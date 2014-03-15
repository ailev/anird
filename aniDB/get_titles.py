#!/usr/bin/python

import os
from urllib import urlretrieve
import gzip

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
        print "File transfer is done! (%s bytes)" % total
    else:
        print "File transfer in progress (%s bytes)" % transfered

def main():
    if not os.path.isfile( TITLES_XML_GZ_LOCALFILE ):
        urlretrieve( TITLES_XML_GZ_URL, TITLES_XML_GZ_LOCALFILE, retrieve_hook )
    else: 
        print "file %s is already present" % TITLES_XML_GZ_LOCALFILE
    
    if not os.path.isfile( TITLES_XML_LOCALFILE ):
        f = gzip.open( TITLES_XML_GZ_LOCALFILE, 'rb')
        file_content = f.read()
        f.close()
        
        fout = open( TITLES_XML_LOCALFILE, 'wb' )
        fout.writelines( file_content )
        fout.close()
        print "file %s is ready" % TITLES_XML_LOCALFILE
    else: 
        print "file %s is already present" % TITLES_XML_LOCALFILE


main()
