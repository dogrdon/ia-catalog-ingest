inkwork ingest types
====================

These are the different types and thus will probably have to be brought in separately:

item:
	* title
	* description
	* date
	* size

entities *should these be added first?*:
	* photographer, (relationship_typeid=185) 
	* designer, (relationship_typeid=172)
	* client, (relationship_typeid=PENDING???)
	* source artist(?), (relationship_typeid=171)
	* creator='inkworks', (relationship_typeid=92) (or printer, (r_tid=175))

representations (relationship_typeid=463?):
	- filename

lots (relationship_typeid=object->collection->lot=134???) **just create one and refer to it per object**
	-lot (id=305)

storage locations (relationship_typeid=19)
	- location=??? (id=???)
