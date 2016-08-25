import json
import sys
import config
import requests

__USER = config.__USER
__PASS = config.__PASS
target_url = 'https://catalog.interferencearchive.org/service.php/item/ca_entities/id/%s'


def find_dupes(filename):
	dupes = {}
	with open(filename, 'r') as infile:
		data = json.loads(infile.read())
		for d in data['results']:
			dupes.setdefault(d['display_label'], []).append(d['entity_id'])
	for d,v in dupes.items():
		if len(v) < 2:
			del dupes[d]
	return dupes

def check_record(entity_id_list):
	d = {}
	for eid in entity_id_list:
		res = requests.get((target_url % eid), auth=(__USER, __PASS))
		try: 
			r = res.content['results']
			if 'related' in r.keys()
				d[eid] = True
			else:
				d[eid] = False
		except e:
			sys.exit(e)
	return d


def filter_dupes(datastore):
	checked = []
	for k,v in datastore.items():
		res = check_record(v)
		checked.append(res)
	return checked

if __name__ == '__main__':

	f = sys.argv[1] #file to id dupes
	
	# loop through ca_entities.json

	# count all the entities by display_label -> store in another array by count

	# delete any entities with count < 2

	# this is your list of entities that need to be checked for deletion....

	dupe_store = find_dupes(f)

	# with deletion list, 

	# check entity through API

	# if entity DOES NOT have a related property

	# AND

	# the other one does

	# store id in list for deletion

	deletion_list = filter_dupes(dupe_store)

	# delete whichever does not have relateds or just leave one (if both no relateds)


