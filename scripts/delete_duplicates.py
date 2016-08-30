'''ad hoc script for removing duplicate entities (for now) from IA collective access.
	1) pulls down all entities from web service api and figures out dupes merely by matching display_labels (doesn't capture alternative spellings etc)
	2) checks if of the dupes there is one with established relationships and others with nothing, it will delete the ones w/o relationships
	3) run first time to get the list
	4) run again with `-r` to do the deletions
	5) may be left with a few dupes where both have relationships, these, for now, have to be dealt with manually - hopefully not a large number of these'''

import json
import sys, os
import config
import requests
import argparse
import time
import pickle

parser = argparse.ArgumentParser(description='Command line tool for deleting duplicate entities from a collective access installation using the web service api')
parser.add_argument('-r', '--runnow', help='Use this flag ', required=False, action="store_true")
args = vars(parser.parse_args())

RUNNOW = args['runnow']

__USER = config.__USER
__PASS = config.__PASS
DELETION_STORE = './pickles/deletion_list.pickle'
entities_all = 'https://catalog.interferencearchive.org/admin/service.php/find/ca_entities?q=*'
target_url = 'https://catalog.interferencearchive.org/admin/service.php/item/ca_entities/id/%s'



def find_dupes(entities):
	dupes = {}
	
	data = json.loads(entities.content)
	for d in data['results']:
		dupes.setdefault(d['display_label'], []).append(d['entity_id'])
	for d,v in dupes.items():
		if len(v) < 2:
			del dupes[d]
	return dupes

def check_record(entity_id_list):
	d = {}
	print("checking: ", entity_id_list)
	for eid in entity_id_list:
		res = requests.get((target_url % eid), auth=(__USER, __PASS))
		r = json.loads(res.content)
		if 'related' in r.keys():
			d[eid] = True
		else:
			d[eid] = False
	return d


def filter_dupes(datastore):
	delete_me = []
	for k,v in datastore.items():
		res = check_record(v)
		for k,v in res.items():
			if not v and True in res.values():       #delete all that have no relationships where at least one does
				delete_me.append(k)
			elif not v and not True in res.values(): #or if no relationships for any, just keep the head item
				res_tail = res[1:]
				delete_me.extend(res_tail)
			else: 
				print("May need to inspect for manual deletion: ", res)
	return delete_me 

def delete_entities(delete_list):
	for i in delete_list:
		delete_url = target_url % i
		time.sleep(2)
		try:
			print("deleting entity with id: ", i)
			r = requests.delete(delete_url, auth=(__USER, __PASS))
			if r.status_code == 200 and r.content == ('{"ok":true,"deleted":"%s"}' % i):
				print(i, " successfully deleted")
			else:
				print("something went wrong: ", r.content)
		except requests.exceptions.RequestException as e:    # This is the correct syntax
			sys.exit(e)
	
	#after we've run this, delete the pickle
	print("wrapping up and deleting the store of keys to delete")
	os.remove(DELETION_STORE)

if __name__ == '__main__':
	
	# loop through ca_entities.json

	# count all the entities by display_label -> store in another array by count

	# delete any entities with count < 2

	# this is your list of entities that need to be checked for deletion....

	dupe_store = find_dupes(requests.get((entities_all), auth=(__USER, __PASS)))

	# with deletion list, 

	# check entity through API

	# if entity DOES NOT have a related property

	# AND

	# the other one does

	# store id in list for deletion

	if os.path.isfile(DELETION_STORE):
		deletion_list = pickle.load( open( DELETION_STORE, "rb" ) )
	else:
		deletion_list = filter_dupes(dupe_store)
		pickle.dump( deletion_list, open( DELETION_STORE, "wb" ) )

	
	# delete whichever does not have relateds or just leave one (if both no relateds)
	
	if RUNNOW:
		delete_entities(deletion_list)
	elif len(deletion_list) == 0:
		print("No dupes, congratulations!")
	else:
		print("Runnning command with `-r`, You will delete %s items: %s" % (str(len(deletion_list)), str(deletion_list)) )


