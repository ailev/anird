from flask import Flask
from flask import request, url_for, render_template
import jinja2
import time
import tornado
import tornado.httpserver
import tornado.wsgi

app = Flask(__name__)
app.debug = True

app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('extensions/GoogleExt/templates'),
])

class MyWSGIContainer(tornado.wsgi.WSGIContainer):
	def _log(self, status_code, request):
		pass

import threading, Queue, ctypes
container = MyWSGIContainer(app)
http_server = tornado.httpserver.HTTPServer(container)

class FlaskThread(threading.Thread):

	def run(self):
		global http_server
		http_server.listen(5000)
		tornado.ioloop.IOLoop.instance().start()
		http_server.stop()

	def stop(self):
		global http_server
		tornado.ioloop.IOLoop.instance().stop()

flask_thread = None

@public('workbench.menubar')
class xWebMenu:
    vis_label = "Web"
    menu_content = 'dot15926.menu.web_menu'
    position = 11

@public('dot15926.menu.web_menu')
class xMenuGoogleWebView:
    vis_label = "Start/stop google web view"
    menu_check = True

    @classmethod
    def Do(cls):
    	global flask_thread
    	if flask_thread:
    		flask_thread.stop()
    		flask_thread = None
    	else:
            flask_thread = FlaskThread()
            flask_thread.daemon = True
            flask_thread.start()

    @staticmethod
    def Update(action):
    	global flask_thread
        action.setChecked(flask_thread != None)


#good code begins
#####################################################
from iso15926 import EnvironmentContext
import traceback

@app.route("/")
def hello():
	try:
		return render_template('index.html')
	except:
		public.report_err()
		return traceback.format_exc()

COLLECT_QUERY = """
i=builder.collect(type=patterns.GoogleRoute.base, name_loc1=val1, name_loc2=val2)
items = find(id = i, type='http://posccaesar.org/rdl/RDS11589310')
result = {}
for v in items:
	try:
		result[v] = find(id=v, label=out).pop()
	except:
		pass
"""

ROUTE_QUERY = """
itemname = ''
try:
	itemname = find(id=uri, label=out).pop()
except:
	pass
items = find(type=patterns.Composition, whole=uri, part=out)
result = {}
for v in items:
	try:
		result[v] = find(id=v, label=out).pop()
	except:
		pass
"""

POINT_QUERY = """
itemname = ''
try:
	itemname = find(id=uri, label=out).pop()
except:
	pass
items = find(type=patterns.Composition, whole=out, part=uri)
result = {}
for v in items:
	try:
		result[v] = find(id=v, label=out).pop()
	except:
		pass
"""

@app.route('/q',methods = ['GET'])
def q():
	try:
		val1 = request.args.get('val1')
		val2 = request.args.get('val2')
		if not val1 or not val2:
			return "All arguments required!!!"
		ec = EnvironmentContext(None, dict(val1=val1, val2=val2))
		ec.ExecutePythonString2(COLLECT_QUERY)
		return render_template('q.html', items=ec.GetLocals()['result'])
	except:
		public.report_err()
		return traceback.format_exc()
 

@app.route('/route',methods = ['GET'])
def route():
	try:
		uri = request.args.get('uri')
		if not uri:
			return "All arguments required!!!"
		ec = EnvironmentContext(None, dict(uri=uri))
		ec.ExecutePythonString2(ROUTE_QUERY)
		return render_template('route.html', items=ec.GetLocals()['result'], name = ec.GetLocals()['itemname'])
	except:
		public.report_err()
		return traceback.format_exc()

@app.route('/point',methods = ['GET'])
def point():
	try:
		uri = request.args.get('uri')
		if not uri:
			return "All arguments required!!!"
		ec = EnvironmentContext(None, dict(uri=uri))
		ec.ExecutePythonString2(POINT_QUERY)
		return render_template('point.html', items=ec.GetLocals()['result'], name = ec.GetLocals()['itemname'])
	except:
		public.report_err()
		return traceback.format_exc()