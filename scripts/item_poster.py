#!/usr/bin/env python

"""script for ingesting items into collective access.

   to run: python item_poster.py -i [path_to_ca_items_all]
"""

import csv, json
import os, sys, time
import requests
import config
import argparse
import ca_client

__USER = config.__USER
__PASS = config.__PASS

def main(arguments):
	parser = argparse.ArgumentParser(description=__doc__,
	                                 formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-i', '--infile', help="Input file", type=argparse.FileType('r'))
	parser.add_argument('-t', '--test', help="Test Run Only", action="store_true")

	args = parser.parse_args(arguments)
	infile = args.infile
	TEST = args.test
	
	ca = ca_client.CollectiveAccess(__USER, __PASS)

	with infile:
		data = json.load(infile)
		for i in data:
			time.sleep(2)
			r = ca.create_object(json.dumps(i))
			if r.status_code == 200:
				result = json.loads(r.content)
				print result
			else:
				sys.exit("couldn't post item: ", r.content)


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
			
				


				