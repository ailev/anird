import xml.etree.ElementTree as ET
import requests
import re
import time
from os import path

base_dir = path.dirname( __file__ );
data_dir = path.join( base_dir, 'data' )


ANN_REPORTS_URL = 'http://www.animenewsnetwork.com/encyclopedia/reports.xml'

@public('collectors.ANNTitle')
def handler(params, pattern_name):
	root = None
	if 'nlist' in params:
		if params['nlist'] == 'all':
			if path.exists(path.join( data_dir, 'reports.xml' )):
				tree = ET.parse(path.join( data_dir, 'reports.xml' ))
				if tree:
					root = tree.getroot()
		else:
			payload = {'id': '155', 'nlist': params['nlist']}
			result = requests.get(ANN_REPORTS_URL, params=payload)
			if result.status_code == 200:
				root = ET.fromstring(result.content)

	if root is not None:		
		for item in root.findall('item'):
			title = item.find('name').text
			id = item.find('id').text
			vintage = item.find('vintage')
			year = None
			if vintage is not None:
				year = vintage.text.split('-')[0]
			yield { 'Title' : title, 'TitleId' : id, 'Year' : year  }

ANN_API_URL = 'http://www.animenewsnetwork.com/encyclopedia/api.xml'

@public('collectors.ANNTitleDetails')
def handler2(params, pattern_name):
	if 'title' in params:
		payload = {'title': params['title']}
		result = requests.get(ANN_API_URL, params=payload)
		if result.status_code == 200:
			root = ET.fromstring(result.content)
			for item in root.findall('anime') + root.findall('manga'):
				id = item.attrib['id']
				title = None
				for info in item.findall('info'):
					if 'Main title' in info.attrib:
						title = info.text
				
				vintage = item.find('vintage')
				year = None
				if vintage is not None:
					year = vintage.text.split('-')[0]
				
				for staff in item.findall('staff'):
					position = staff.find('task').text
					person_id = staff.find('person').attrib['id']
					person_name = staff.find('person').text
					yield { 
					'TitleId' : id
					, 'PositionName' : position
					, 'PersonId' : person_id
					, 'PersonName' : person_name
					}
