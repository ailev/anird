import xml.etree.ElementTree as ET
import os, sys
from os import path
from urllib import urlretrieve
import gzip
import time
import requests
from extensions.aniDB import *

base_dir = path.dirname( __file__ );
data_dir = path.join( base_dir, 'data' )

@public('collectors.AniDBTitle')
def handler(params):
	filename = path.join(data_dir, 'anime-titles.xml')
	tree = ET.parse(filename)
	if tree:
		root = tree.getroot()
		count = params.get('nlist')
		counter = 0
		for item in root.findall('anime'):
			if count and counter == count:
				return
			counter += 1
			title_main = None
			titles_other = []
			for info in item.findall('title'):
				if info.attrib.get('type') == 'main':
					title_main = info.text
				titles_other.append((info.attrib.get('type'), info.text))

			id = item.attrib.get('aid')
			if title_main:
				yield { 'TitleMain' : title_main, 'TitleId' : id}
				for title_other_type, title_other in titles_other:
					yield { 'TitleMain' : title_main, 'TitleId' : id, 'TitleTypeName': title_other_type, 'Title': title_other}


@public('collectors.AniDBTitleDetails')
def handler2(params):
	if 'title' in params:
		filename = AniDB().get_anime(params['title'])
		if filename:
			tree = ET.parse(filename)
			root = tree.getroot()
			id = params['title']

			for staff in root.find('creators').findall('name'):
				position = staff.attrib['type']
				person_id = staff.attrib['id']
				person_name = staff.text

				yield { 
				'TitleId' : str(id)
				, 'PositionName' : position
				, 'PersonId' : person_id
				, 'PersonName' : person_name
				}


