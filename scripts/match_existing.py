import csv, json
import os, sys
import requests
from fuzzywuzzy import fuzz

__USER = config.__USER
__PASS = config.__PASS
entities_all = 'https://catalog.interferencearchive.org/admin/service.php/find/ca_entities?q=*'



if __name__ == '__main__':
	main()