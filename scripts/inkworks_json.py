
#!/usr/bin/env python

"""script for converting csv file of inkworks records into
   collective access compliant json for ingest.

   to run: python inkworks.py [path to inkworks csv] -o [path to output].json
"""

import os, sys
import argparse
import csv
import requests
import config

CA_RELATIONSHIP_IDS = {"lot_id": 134,
                   "client_id": 202,
                   "photographer_id": 185,
                   "designer_id": 172,
                   "sourceartist_id": 171,
                   "storage_id": 'NA'}
LOT_ID = 305 #not sure if this is how lot relationships are assigned.
NEW_ITEM_TYPE_ID = 435

def handle_entity(entities):
    pass

def make_item(row):
    item = {'intrinsic_fields':{}, 'preferred_labels':[], 'attributes':{
                                                                        'notes':[],
                                                                        'titleType':[],
                                                                        'dataSet':[],
                                                                        'measurements_field':[]
    }, 'related':{}}
    image = row['filename']
    idno = image.split('.')[0] #for matching media on upload, give it the filename id
    item['intrinsic_fields']['idno'] = idno
    item['intrinsic_fields']['type_id'] = NEW_ITEM_TYPE_ID
    item['preferred_labels'].append({"locale" : "en_US", "name" : row['title']})
    item['attributes']['notes'].append({"locale" : "en_US", "name" : row['notes']})
    item['attributes']['titleType'].append({"locale" : "en_US", "name" : row['title']})
    item['attributes']['dateSet'].append({"locale" : "en_US", "name" : row['date']})
    item['attributes']['measurements_field'].append({"locale" : "en_US", "name" : row['size']})
    # RIGHTS?

def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    infile = args.infile
    outfile = args.outfile

    with infile:
    	reader = csv.DictReader(infile)
    	header = reader.fieldnames

        items = []

        for row in reader:


        data = json.dumps(items, indent=4)

        with open(outfile, 'w') as outf:
            outf.write(data)


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
