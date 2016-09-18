

###################################### info ###################################
# Used to take in csv (tab separated here) of names that might be entities 
# in our Collective Access instance
# Employs fuzzywuzzy (https://github.com/seatgeek/fuzzywuzzy) to determine 
# if that name is already in a dump of all entities in the system prints results
# to STDOUT because there aren't a ton and we want to review the results.
# Could be a smarter script
# Run as `python match_existing.py [Path to tsv with names in first column]`
###############################################################################

import csv, json
import os, sys
import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import utils
import config

__USER = config.__USER
__PASS = config.__PASS
entities_all = 'https://catalog.interferencearchive.org/admin/service.php/find/ca_entities?q=*'

infile = sys.argv[1]

if __name__ == '__main__':

	catalog_entities = json.loads(requests.get((entities_all), auth=(__USER, __PASS)).content)['results']
	catalog_data = {i['display_label']:i['entity_id'] for i in catalog_entities}
	with open(infile, 'r') as f:
		rows = csv.reader(f, delimiter='\t')
		rows.next()
		for row in rows:
			for k,v in catalog_data.items():
				iw = utils.asciidammit(row[0])
				score = fuzz.ratio(iw, k)
				if score > 75:
					print iw, "-----", k, v
