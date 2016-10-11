#!/usr/bin/env python

"""script for converting csv file of inkworks records into
   collective access compliant json for ingest.

   to run: python entity_maker.py -i [path_to_ca_entities_all.tsv] -o [path_to_new_entities.tsv]
"""

import csv, json
import os, sys
import requests
import config
import argparse
import ca_client

__USER = config.__USER
__PASS = config.__PASS


def make_entity(row):
	entry = {'intrinsic_fields':{}, 'preferred_labels':[]}
	
	idno = "inkworks_ent_{0}".format(row['pkey'])
	entry['intrinsic_fields']['idno'] = idno
	if row['type'].strip() == 'ind':
		
		entry['intrinsic_fields']['type_id'] = 80

		name = [r.strip() for r in row['entity'].split(' ')]
		
		if len(name) == 1:
			surname = name[0] #collective access requires that at least the surname exists
			middlename = forename = ""
		elif len(name) == 2:
			forename, surname = name
			middlename = ""
		elif len(name) == 3:
			forename, middlename, surname = name
		else:
			surname = name.pop()
			forename = (" ").join(name)

		pref_labels = {"locale" : "en_US",
					   "forename" : forename, 
					   "middlename" : middlename,
					   "surname" : surname
					   } 

		entry['preferred_labels'].append(pref_labels)

	elif row['type'].strip() == 'org':
		entry['intrinsic_fields']['type_id'] = 81

		org_name = row['entity']
		pref_labels = {"locale" : "en_US",
					   "forename" : "", 
					   "middlename" : "",
					   "surname" : org_name
					   }
		entry['preferred_labels'].append(pref_labels)
	else:
		entry = None

	return entry

def post_entity(client, entity):
	
	entity = json.dumps(entity)

	try:
		print("adding entity with: ", entity)
		r = client.create_entity(entity)
		if r.status_code == 200:
			result = json.loads(r.content)
			print result
			entity_id = result['entity_id']
			print(entity_id, " successfully added")
			return entity_id
		else:
			entity_id = None

	except requests.exceptions.RequestException as e:   
		sys.exit("An unexpected error occurred", e)


def main(arguments):
	parser = argparse.ArgumentParser(description=__doc__,
	                                 formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-i', '--infile', help="Input file", type=argparse.FileType('r'))
	parser.add_argument('-o', '--outfile', help="Output file",
	                    default=sys.stdout, type=argparse.FileType('w'))
	parser.add_argument('-t', '--test', help="Test Run Only", action="store_true")

	args = parser.parse_args(arguments)
	infile = args.infile
	outfile = args.outfile
	TEST = args.test
	
	ca = ca_client.CollectiveAccess(__USER, __PASS)

	with infile:
		with outfile:
			rows = csv.DictReader(infile, delimiter='\t')
			cols = rows.fieldnames
			writer = csv.writer(outfile, delimiter='\t')
			writer.writerow(cols)
			
			for row in rows:
				if row['catalog_id'].strip() == "":
					entity = make_entity(row)
					if entity != None:
						row['catalog_id'] = post_entity(ca, entity)
					else:
						row['catalog_id'] = 'FAILED!'
						sys.exit("something went wrong with adding this entity, exiting: ", row)

				new_row = [row[i] for i in cols]
				writer.writerow(new_row)


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
			
				


				