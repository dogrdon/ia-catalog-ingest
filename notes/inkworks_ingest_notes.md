inkwork ingest types
====================

These are the different types and thus will probably have to be brought in separately:

item:
	* title
	* description
	* date
	* size

entities *should these be added first?*: 
	what about individual or organization? (ind = 80, org = 81)
	* photographer, (relationship_typeid=185) 
	* designer, (relationship_typeid=172)
	* client, (relationship_typeid=202)
	* source artist(?), (relationship_typeid=171)
	* creator='inkworks', (relationship_typeid=92) (or printer, (r_tid=175))

representations (relationship_typeid=463?):
	- filename

lots (relationship_typeid=object->collection->lot=134???) **just create one and refer to it per object**
	-lot (id=305)

storage locations (relationship_typeid=19)
	- location=??? (id=???)


#### Data Cleaning Notes

0. Split what appear to be multiple entities originally in a single line into their own column

1. Run typical clustering (OpenRefine) to merge entities with typos, different spellings

2. Standardize orgs with {FULLNAME} ({ACRONYM})

3. Remove hidden characters (e.g., )

4a. Send entities to their own sheets (normalize) Note: clients can also be designers.

4b. Note whether entities are people or organizations.

5. Find which entities are already in CA catalog (query entities, see **Other issues**)



#### Other issues:

**DELETE DUPLICATES:** See [`scripts/delete_duplicates.py`]

Need to remove duplicate entries (see list below). If we have ids for duplicate entries, we can query the Web Service API for each one with:

    curl -XGET 'https://{user}:{pass}@catalog.interferencearchive.org/admin/service.php/item/ca_entities/id/{id}?&pretty=1'

if the returned JSON has a `related` property, don't delete.

else (soft delete):

    curl -XDELETE 'http://{user}:{pass}@catalog.interferencearchive.org/service.php/item/ca_entities/id/{id}?pretty=1'

**MATCH ENTITIES IN INGEST WITH THOSE ALREADY IN COLLECTIVE ACCESS:**
