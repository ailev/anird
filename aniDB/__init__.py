# getting data from AniDB.net

import os, sys
from os import path
from urllib import urlretrieve
import gzip
import time
import requests

base_dir = path.dirname( __file__ );
data_dir = path.join( base_dir, 'data' )

ANIDB_CLIENT_NAME="anird"
ANIDB_CLIENT_VER=0
ANIDB_HTTP_PROTOVER=1
ANIDB_HTTP_API_URL="http://api.anidb.net:9001/httpapi?client=%s&clientver=%d&protover=%d&" % (ANIDB_CLIENT_NAME, ANIDB_CLIENT_VER, ANIDB_HTTP_PROTOVER )

class AniDB():
	def get_titles(self):
		'''get anime-titles.xml'''

	def get_anime(self,id):
		'''get anime details by id from the HTTP API'''
		print "get anime", id
		
		filename_xml = path.join( data_dir, "%d.xml" % id )
		
		if path.isfile(filename_xml):
			return filename_xml
			
		# request from the HTTP API
		url = ANIDB_HTTP_API_URL + "request=anime&aid=" + id
		print "url:", url

		# save into the data_dir
		r = requests.get( url )
		xml = r.content;

		fout = open( filename_xml, 'wb' )
		fout.writelines( xml )
		fout.close()

		# return the filename
		if path.isfile(filename_xml):
			return filename_xml

