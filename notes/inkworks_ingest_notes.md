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
	* client, (relationship_typeid=PENDING???)
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

Need to remove duplicate entries (see list below). If we have ids for duplicate entries, we can query the Web Service API for each one with:

    curl -XGET 'https://{user}:{pass}@catalog.interferencearchive.org/admin/service.php/item/ca_entities/id/{id}?&pretty=1'

if the returned JSON has a `related` property, don't delete.

else (soft delete):

    curl -XDELETE 'http://{user}:{pass}@catalog.interferencearchive.org/service.php/item/ca_entities/id/{id}?pretty=1'

The following entities already in CA have duplicate entries:

The Last Emperor	6
Chuck Munson	4
Doug Moss	4
Hi-Tek	4
Sister Asia	4
Ed O.G.	3
Out Of Order Books	3
Sophia Nachala	3
The Art Institute Of Chicago	3
7U?	2
A3BC	2
Alex Chechile	2
Amanda Richardson	2
Amy Halbohm	2
Anarchist Association Of The Americas	2
Arra Lynn Ross	2
Art Pluribus Unum	2
B Kite	2
Bahamadia	2
Barricada Collective	2
Big Noise Tactical Media	2
Bruce Langhorne	2
Carrie McNinch	2
Cedar Nordbye	2
Chris Kasper	2
Chris Larson	2
Christopher E Kubasik	2
Coalition Against Israeli Apartheid	2
Dan Tanz	2
David Gahr	2
Doug Minkler	2
Ed Epstein	2
Eric Kjensrud	2
Feral Children Productions LLC	2
Fireworks Graphics Collective	2
Ginger Brooks Takahashi	2
James Bell	2
Jean Hart	2
Jean Smith	2
Joel Herron	2
John Chu	2
Lindsay Starbuck	2
Lorraine Perlman	2
Lourdes Lugo	2
Lynne Stewart	2
Malaquias Montoya	2
Marc Jay	2
Margaret Killjoy	2
Mchawi Basir	2
Mike Zoot	2
Mr. Man	2
Nathan Meltz	2
Obscurist Press	2
Ojore Lutalo	2
P.E.A.C.E.	2
People's Communications Committee	2
Peter Chow	2
Pyro	2
Radical America	2
Rah Digga	2
Reinie Press	2
Shabaam Sahdeeq	2
Steven Dominici Prestianni	2
Toyo Obayashi	2
Xzibit	2
Yuko Tohohira	2