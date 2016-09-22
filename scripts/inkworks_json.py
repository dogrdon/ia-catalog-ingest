#!/usr/bin/env python

"""script for converting csv file of inkworks records into
   collective access compliant json for ingest.

   to run: python inkworks.py -i [path_to_inkworks.csv] -o [path_to_output.json]
"""

import os, sys
import argparse
import csv, json
import requests
import config

CA_RELATIONSHIP_IDS = {"lot_id": 60,
                       "client_id": 202,
                       "photographer_id": 185,
                       "designer_id": 172,
                       "sourceartist_id": 171,
                       "format_id": 195}
LOT_ID = 305 
NEW_ITEM_TYPE_ID = 435
LIST_ID = 57
ITEM_ID = 329

ENTITY_STORE = '../data/inkworks/new_entities.csv'
ENTITIES = {row['entity']:row['catalog_id'] for row in csv.DictReader(open(ENTITY_STORE, 'r'), delimiter='\t')}
clients = ['client_1', 'client_2', 'client_3', 'client_4']
designers = ['designer_1', 'designer_2', 'designer_3']
photographers = ['photographer_1', 'photographer_2']
source_artists = ['source_artist_1', 'source_artist_2', 'source_artist_3', 'source_artist_4']


def handle_entities(entities, relation_type):
    return [{'entity_id':ENTITIES[entity], 'type_id':relation_type} for entity in entities if entity in ENTITIES.keys()]


def make_item(row, test=False):
    keys = row.keys()
    item = {'intrinsic_fields':{}, 
            'preferred_labels':[], 
            'attributes':{
                'notes':[],
                'dateSet':[],
                'measurements_field':[],
                'rightsSet':[]
            }, 
            'related':{'ca_entities' : [], 
                       'ca_object_lots':[{'lot_id':LOT_ID, 'type_id':CA_RELATIONSHIP_IDS['lot_id']}],
                       'ca_list_items' : [{'list_id':LIST_ID, 'item_id':ITEM_ID, 'type_id':CA_RELATIONSHIP_IDS['format_id']}]
                      }}

    image = row['filename']
    idno = row['idno'] #for matching media on upload, give it the filename id
    
    if test:
        item['intrinsic_fields']['idno'] = "TEST_"+idno
    else:
        item['intrinsic_fields']['idno'] = idno

    item['intrinsic_fields']['type_id'] = NEW_ITEM_TYPE_ID
    item['preferred_labels'].append({"locale" : "en_US", "name" : row['title']})
    if row['notes'] != '':
        item['attributes']['notes'].append({"locale" : "en_US", "notes" : row['notes']})
    if row['date'] != '':
        item['attributes']['dateSet'].append({"locale" : "en_US", "dateSet" : row['date']})
    if row['size'] != '':
        item['attributes']['measurements_field'].append({"locale" : "en_US", "measurements_field" : row['size']})
    if row['rights'] != '':
        item['attributes']['rightsSet'].append({"locale" : "en_US", "rightsSet" : row['rights']})

    row_clients = ([row[i] for i in clients if i != ''], CA_RELATIONSHIP_IDS['client_id'])
    row_designers = ([row[i] for i in designers if i != ''], CA_RELATIONSHIP_IDS['designer_id'])
    row_photographers = ([row[i] for i in photographers if i != ''], CA_RELATIONSHIP_IDS['photographer_id'])
    row_source_artists = ([row[i] for i in source_artists if i != ''], CA_RELATIONSHIP_IDS['sourceartist_id'])

    relateds = [row_clients, row_designers, row_photographers, row_source_artists]

    for r in relateds:
        if r[0] != []:
            item['related']['ca_entities'].extend(handle_entities(r[0], r[1]))
    return item

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

    with infile:
    	reader = csv.DictReader(infile, delimiter='\t')
    	header = reader.fieldnames

        items = []

        for row in reader:
            items.append(make_item(row, TEST))

        data = json.dumps(items, indent=4)

    with outfile:
        outfile.write(data)


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
