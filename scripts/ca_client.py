import requests
import json

class CAClient(object):
	"""creates a session for collective access actions"""
	def __init__(self, user, passw, header={'content-type':'application/json'}):
		super(CAClient, self).__init__()
		self.user = user
		self.passw = passw
		self.header = header
		self.sesh = requests.session()
		self.sesh.auth = (self.user, self.passw)
		
	def get_entities(self):
		pass

	def get_entitiy(self, entity_id):
		pass

	def get_objects(self):
		pass

	def get_object(self, object_id):
		pass

	def create_entity(self, data):
		target = 'https://catalog.interferencearchive.org/admin/service.php/item/ca_entities'
		return self.sesh.put(target,data=data, headers=self.header)
	
	def create_object(self, data):
		target = 'https://catalog.interferencearchive.org/admin/service.php/item/ca_objects'
		return self.sesh.put(target,data=data, headers=self.header)