
#!/usr/bin/env python

"""script for converting csv file of inkworks records into
   collective access compliant json for ingest.

   to run: python inkworks.py [path to inkworks csv] -o [path to output].json
"""

import os, sys
import argparse
import csv


def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    infile = args.infile

    with infile:
    	reader = csv.DictReader(infile)
    	header = reader.fieldnames
	'''continue to do stuff that pulls everything into place'''


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
