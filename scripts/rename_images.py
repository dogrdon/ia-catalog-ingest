import os
import csv

f = '../data/inkworks/inkworks_ingest_tail.tsv'
images = '../data/inkworks/poster_images'

def main():
	with open(f, 'r') as infile:
		reader = csv.DictReader(infile, delimiter='\t')
		image_name_map = {}
		for row in reader:
			image_name_map[row['filename']] = row['idno'] 	

	filenames = os.listdir(images)
	for filename in filenames:
		if filename in image_name_map.keys():
			ext = filename.split('.')[1]
			new_filename = image_name_map[filename]+"."+ext
			old_path = os.path.join(images, filename)
			new_path = os.path.join(images, new_filename)
			os.rename(old_path, new_path)


if __name__ == '__main__':
	main()