import xml.etree.ElementTree as ET
import os, sys
from os import path
from urllib import urlretrieve
import gzip
import time
import requests

base_dir = path.dirname( __file__ );
data_dir = path.join( base_dir, 'data' )

@public('collectors.AnnTitle')
def handler(params):
	filename = path.join(data_dir, 'anime-titles.xml')
	tree = ET.parse(filename)
	if tree:
		root = tree.getroot()
		for item in root.findall('anime'):
			title = None
			for info in item.findall('title'):
				if info.attrib.get('type') == 'official' and info.attrib.get('xml:lang') == 'en':
					title = info.text

			id = item.attrib.get('aid')
			if title:
				yield { 'Title' : title, 'AniDB_TitleId' : id}


@public('collectors.AniDB_Details')
def handler(params):
	if 'title' in params:
		filename = AniDB().get_anime(params['title'])
		if filename:
			tree = ET.parse(filename)
			root = tree.getroot()

			for item in root.findall('anime') + root.findall('manga'):
				id = params['title']

				title = None
				for info in item.findall('title'):
					if info.attrib.get('type') == 'main':
						title = info.text

				year = item.find('startdate').text.split('-')[0]
				
				for staff in item.find('creators').findall('name'):
					position = staff.attrib['type']
					person_id = staff.attrib['id']
					person_name = staff.text
					yield { 
					'Title' : title
					, 'TitleId' : id
					, 'Year' : year  
					, 'PositionName' : position
					, 'PersonId' : person_id
					, 'PersonName' : person_name
					}


