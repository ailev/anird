# getting data from AniDB.net

import os, sys
from os import path
from urllib import urlretrieve
import gzip
import time

base_dir = path.dirname( __file__ );
data_dir = path.join( base_dir, 'data' )

class AniDB():
	def get_titles(self):
		'''get anime-titles.xml'''

	def get_anime(self,id):
		'''get anime details by id from the HTTP API'''
		print "get anime %d" % id

