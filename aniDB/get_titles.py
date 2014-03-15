#!/usr/bin/python

import os, sys
from urllib import urlretrieve
import gzip
import time

base_dir = os.path.dirname( __file__ );

# test values
if 1:
	TITLES_XML_GZ_URL = 'http://ahinea.com/qvwm/qvwm-1.1.12-9-IKu.tar.gz'
	TITLES_XML_GZ_LOCALFILE = 'tmp/qvwm-1.1.12-9-IKu.tar.gz'
	TITLES_XML_LOCALFILE    = 'tmp/qvwm-1.1.12-9-IKu.tar'

# real values
if 1:
	TITLES_XML_GZ_URL = 'http://anidb.net/api/anime-titles.xml.gz'
	TITLES_XML_GZ_LOCALFILE = 'data/anime-titles.xml.gz'
	TITLES_XML_LOCALFILE    = 'data/anime-titles.xml'


def retrieve_hook(count,size,total):
	transfered = count * size
	if transfered >= total:
		print " done! (%s bytes)" % total
	else:
		sys.stdout.write('.')
		sys.stdout.flush()

def main():
	
	url          = TITLES_XML_GZ_URL
	filename_gz  = os.path.join( base_dir, TITLES_XML_GZ_LOCALFILE )
	filename_xml = os.path.join( base_dir, TITLES_XML_LOCALFILE )

	retrieve = False
	update   = False
	
	print "file %s:" % filename_gz
	
	if os.path.isfile( filename_gz ):
		mtime = os.path.getmtime( filename_gz )
		print "...last modified: %s (ctime)" % time.ctime( mtime )
		if time.time() > mtime + 24*60*60:
			print "...more than a day has passed. we can re-request the file now"
			retrieve = True
			update = True
		else:
			print "...is new enough"
	else:
		retrieve = True

	if retrieve:
		urlretrieve( url, filename_gz, retrieve_hook )
	else: 
		print "...no need to download it (again)"
	
	print "file %s:" % filename_xml
	
	if not os.path.isfile( filename_xml ) or update:
		f = gzip.open( filename_gz, 'rb')
		file_content = f.read()
		f.close()
		
		fout = open( filename_xml, 'wb' )
		fout.writelines( file_content )
		fout.close()
		print "...extracted"
		
	if os.path.isfile( filename_xml ):
		print "...ready to be parsed"

main()
