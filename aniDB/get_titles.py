#!/usr/bin/python

import os, sys
from urllib import urlretrieve
import gzip
import time

# test values
if 1:
	TITLES_XML_GZ_URL = 'http://ahinea.com/qvwm/qvwm-1.1.12-9-IKu.tar.gz'
	TITLES_XML_GZ_LOCALFILE = 'tmp/qvwm-1.1.12-9-IKu.tar.gz'
	TITLES_XML_LOCALFILE = 'tmp/qvwm-1.1.12-9-IKu.tar'

# real values
if 1:
	TITLES_XML_GZ_URL = 'http://anidb.net/api/anime-titles.xml.gz'
	TITLES_XML_GZ_LOCALFILE = 'data/anime-titles.xml.gz'
	TITLES_XML_LOCALFILE = 'data/anime-titles.xml'


def retrieve_hook(count,size,total):
	transfered = count * size
	if transfered >= total:
		print " done! (%s bytes)" % total
	else:
		sys.stdout.write('.')
		sys.stdout.flush()

def main():
	
	url          = TITLES_XML_GZ_URL
	filename_gz  = TITLES_XML_GZ_LOCALFILE
	filename_xml = TITLES_XML_LOCALFILE

	retrieve = False
	update   = False
	
	if os.path.isfile( filename_gz ):
		mtime = os.path.getmtime( filename_gz )
		print "last modified: %s (ctime)" % time.ctime( mtime )
		if time.time() > mtime + 24*60*60:
			print "more than a day has passed. we can re-request the file now"
			retrieve = True
			update = True
		else:
			print "it is new enough, no need to download it again"
	else:
		retrieve = True

	if retrieve:
		urlretrieve( url, filename_gz, retrieve_hook )
	else: 
		print "file %s is already present" % filename_gz
	
	if not os.path.isfile( filename_xml ) or update:
		f = gzip.open( filename_gz, 'rb')
		file_content = f.read()
		f.close()
		
		fout = open( filename_xml, 'wb' )
		fout.writelines( file_content )
		fout.close()
		print "file %s is ready" % filename_xml
	else: 
		print "file %s is already present" % filename_xml
		
	if os.path.isfile( filename_xml ):
		print "ready to parse %s" % filename_xml


main()
