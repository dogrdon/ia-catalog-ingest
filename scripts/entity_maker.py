import csv, json
import os, sys
import requests
import config

__USER = config.__USER
__PASS = config.__PASS
infile = sys.argv[1] #'../data/inkworks/ca_entities_all.tsv'
target_url = 'https://catalog.interferencearchive.org/admin/service.php/item/ca_entities'

def make_entity(row):
	entry = {'intrinsic_fields':{}, 'preferred_labels':[]}
	
	if row['type'].strip() == 'ind':
		
		entry['intrinsic_fields']['idno'] = "test"
		entry['intrinsic_fields']['type_id'] = 80

		name = [r.strip() for r in row['entity'].split(' ')]
		
		if len(name) == 1:
			forename = name[0]
			middlename = surname = ""
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
		entry['intrinsic_fields']['idno'] = "test"
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

	return json.dumps(entry)


def post_entity(entity):
	try:
		print("adding entity with: ", entity)
		r = requests.put(target_url, auth=(__USER, __PASS), 
									 data=entity, 
									 headers={'content-type':'application/json'})
		if r.status_code == 200:
			result = json.loads(r.content)
			print result
			entity_id = result['entity_id']
			print(entity_id, " successfully added")
			return entity_id
		else:
			entity_id = None
			print("something went wrong: ", r.content)
			return entity_id
	except requests.exceptions.RequestException as e:    # This is the correct syntax
		sys.exit(e)




if __name__ == '__main__':
	
	with open(infile, 'r') as f:
		with open('../data/inkworks/new_entities.csv', 'w') as outfile:
			rows = csv.DictReader(f, delimiter='\t')
			cols = rows.fieldnames
			writer = csv.writer(outfile, delimiter='\t')
			writer.writerow(cols)
			
			for row in rows:
				if row['catalog_id'].strip() == "":
					entity = make_entity(row)
					if entity != None:
						entity_id['catalog_id']= post_entity(entity)
					else:
						entity_id['catalog_id'] = 'FAILED!'

				new_row = [row[i] for i in cols]
				writer.writerow(new_row)
				

			
				


				