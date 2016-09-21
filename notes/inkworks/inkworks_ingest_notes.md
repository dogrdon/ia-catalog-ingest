inkwork ingest types
====================

These are the different types and thus will probably have to be brought in separately:

item (id = 435):

	* title
	* description
	* date
	* size

entities *should these be added first?*: 

	what about individual or organization? (ind = 80, org = 81)

	* photographer, (relationship_typeid=185) 
	* designer, (relationship_typeid=172)
	* client, (relationship_typeid=202)
	* source artist, (relationship_typeid=171)
	* creator='inkworks', (relationship_typeid=92) (or printer, (r_tid=175))

representations (relationship_typeid=463?):

	- filename

lots (relationship_typeid=60) **just create one and refer to it per object**

	-lot (id=305)

format (relationship_typeid=195)
	- format list_id = 57
	- print list_item_id = 329

rights (relationship_typeid=???)
	- there's only a few, perhaps we just do it by hand.

storage locations (relationship_typeid=19)

	- location=??? (id=???)  *NEED TO GET THIS FROM SOMEONE*


#### Data Cleaning Notes

0. Split what appear to be multiple entities originally in a single line into their own column

1. Run typical clustering (OpenRefine) to merge entities with typos, different spellings

2. Standardize orgs with {FULLNAME} ({ACRONYM})

3. Remove hidden characters (e.g., )

4a. Send entities to their own sheets (normalize) Note: clients can also be designers.

4b. Note whether entities are people or organizations.

5. Find which entities are already in CA catalog (query entities, see **Other issues**)

6. Generate entities in json form for Posting and post with (for example): 

	curl -XPUT 'https://{user}:{pass}@catalog.interferencearchive.org/admin/service.php/item/ca_entities' -d '{"preferred_labels": [{"locale": "en_US", "middlename": "", "surname": "TEST Accion Latina TEST", "forename": ""}], "intrinsic_fields": {"idno": "test", "type_id": 81}}'
   
   You should get a success response back with the `entity_id`, so we can store that back with the original record:

    {"ok":true,"entity_id":2055}

7. Clean up objects

8. Will have to assign IA identifies before hand (IA.ITM.###) - get the last item and just add a pkey

9. Move images -- renamed to the corresponding IA.ITM.### `idno` -- into the server location specified on **Import >> Media**, select the directory, and execute the import. This will actually work.

#### Other issues:

**DELETE DUPLICATES:** See [`scripts/delete_duplicates.py`]

Need to remove duplicate entries (see list below). If we have ids for duplicate entries, we can query the Web Service API for each one with:

    curl -XGET 'https://{user}:{pass}@catalog.interferencearchive.org/admin/service.php/item/ca_entities/id/{id}?&pretty=1'

if the returned JSON has a `related` property, don't delete.

else: (soft delete)

    curl -XDELETE 'http://{user}:{pass}@catalog.interferencearchive.org/service.php/item/ca_entities/id/{id}?pretty=1'

image: `3453066.jpg` has no entry 


**UNKNOWN ENTITIES FOR CLARIFICATION**

- CIRRS (client)
- ACD (client)
- ICEF (client)
- tecumo (designer)
- camomile (designer)

**MATCH ENTITIES IN INGEST WITH THOSE ALREADY IN COLLECTIVE ACCESS:**

---based on a fuzzywuzzy fuzz score of >75:

*clients*

- Amnesty International ----- Amnesty International 382
- Inkworks Press ----- Inkworks Press 893
- Prairie Fire Organizing Committee (PFOC) ----- Prairie Fire Organizing Committee 470
- SF Poster Brigade ----- San Francisco Poster Brigade 896
- Terry Forman ----- Terry Forman 1341
- Fireworks ----- Fireworks Graphics Collective 1343

*designers* 

- Doug Minkler ----- Doug Minkler 844
- Emory Douglas ----- Emory Douglas 851
- Favianna Rodriguez ----- Favianna Rodriguez 169
- Inkworks Press ----- Inkworks Press 893
- Jane Norling ----- Jane Norling 1390
- Malaquas Montoya ----- Malaquias Montoya 835
- Rupert Garcia ----- Rupert Garcia 891
- San Francisco Poster Brigade ----- San Francisco Poster Brigade 896
- Terry Forman ----- Terry Forman 1341

*photographers*

- None

*source artists* 

African People's Socialist Party

- Carlos Cortez ----- Carlos Cortez 855
- Malaquias Montoya ----- Malaquias Montoya 835
- Terry Forman ----- Terry Forman 1341
- OSPAAAL (Cuba) ----- OSPAAAL 1353
