#import  extensions.ext_import.import_ext 

import json
import requests
import re
import time


GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
DIRECTIONS_BASE_URL = 'http://maps.googleapis.com/maps/api/directions/json'

def geocode(address):
	payload = {'sensor': 'false', 'address': address}
	result = requests.get(GEOCODE_BASE_URL, params=payload)
	if result.status_code == 200:
		data = json.loads(result.content)
		return [s['formatted_address'] for s in data['results']]


@public('collectors.GoogleExample')
def handler(params, pattern_name):
	if 'address' in params:
		r = geocode(params['address'])
		if r:
			for v in r:
				yield {'address': v}


def getrout(address1, address2):
	payload = {'sensor': 'false', 'origin': address1, 'destination' : address2, 'departure_time' : '1394308900', 'mode' : 'transit'}
	result = requests.get(DIRECTIONS_BASE_URL, params=payload)
	if result.status_code == 200:
		data = json.loads(result.content)
		return data
	else:
		print('No reply from server')
		


@public('collectors.GoogleRoute')
def handler(params, pattern_name):
#	print(pattern_name)
	timestamp =  time.strftime('%X %x')
	if 'name_loc1' in params:
		if 'name_loc2' in params:
			data = getrout(params['name_loc1'], params['name_loc2'])
			if data['status'] == 'OK':

				start_loc = data['routes'][0]['legs'][0]['start_address']
				end_loc = data['routes'][0]['legs'][0]['end_address']
				name_route = 'between ' + start_loc + ' and ' + end_loc 

				all_stops = list()

				all_stops.append(start_loc)

				total_steps = len(data['routes'][0]['legs'][0]['steps'])
				for i in range(total_steps):
					if 'transit_details' in data['routes'][0]['legs'][0]['steps'][i]:
						all_stops.append(data['routes'][0]['legs'][0]['steps'][i]['transit_details']['departure_stop']['name'])
						all_stops.append(data['routes'][0]['legs'][0]['steps'][i]['transit_details']['arrival_stop']['name'])

				all_stops.append(end_loc)

				for i in range(len(all_stops)-1):
#to test external date assignment
					yield({'name_route' : name_route, 'name_loc1': all_stops[i], 'name_loc2': all_stops[i+1],})
# to test internal date assignment
#					yield({'name_route' : name_route, 'name_loc1': all_stops[i], 'name_loc2': all_stops[i+1],  'creation_date' : timestamp})
			else:
				print('No routes found')
				


