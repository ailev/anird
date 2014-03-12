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
    jinja2.FileSystemLoader('extensions/PreviewExt/templates'),
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
class xTextMenuPreview:
    vis_label = "Start/stop preview"
    menu_check = True

    @classmethod
    def Do(cls):
    	global flask_thread
    	if flask_thread:
    		flask_thread.stop()
    		flask_thread = None
    	else:
    		flask_thread = FlaskThread()
    		flask_thread.start()

    @staticmethod
    def Update(action):
    	global flask_thread
        action.setChecked(flask_thread != None)


#good code begins
#####################################################

from collections import namedtuple
from iso15926 import EnvironmentContext, GraphDocument
import traceback

@app.route("/")
def hello():
	try:
		return render_template('sample1.html', ec = EnvironmentContext(None, {}))
	except:
		public.report_err()
		return traceback.format_exc()
 
@app.route('/q',methods = ['GET'])
def q():
	text = request.args.get('text')
	return text

@app.route('/ololo')
def q2():
	return "Ololo happens"
