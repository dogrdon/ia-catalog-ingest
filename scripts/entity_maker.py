import csv, json
import os, sys

infile = sys.argv[1] #'../data/inkworks/ca_entities_all.tsv'

if __name__ == '__main__':
	
	with open(infile, 'r') as f:
		rows = csv.DictReader(f, delimiter='\t')
		cols = rows.fieldnames
		entries = []
		for row in rows:
			entry = {'intrinsic_fields':{}, 'preferred_labels':[]}
			if row['catalog_id'].strip() == "":
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
					print('nothing to do with: ', row)

			entries.append(entry)
			data = json.dumps(entries, indent=4)

		with open('../data/inkworks/new_entities.json', 'w') as outfile:
			outfile.write(data)

				