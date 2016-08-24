Collective Access Data Import Notes
===================================

### 1. Using the Data Importer

[Collective Access documentation for the data importer](http://docs.collectiveaccess.org/wiki/Data_Importer)  -  provides the details, but is light on examples

[Collective Access documentation creating a mapping](http://docs.collectiveaccess.org/wiki/Data_Import:_Creating_and_Running_a_Mapping) - A bit more detail on actually creating the mapping document for the source data ([sample template on google drive](https://docs.google.com/spreadsheets/d/11b_0rkUTm6kTfsC81qICYI6TMlJJ_0JZR9hJODwvEr8/edit))

[Collective Access User Group Sample Workflows and Docs](https://collectiveaccessusers.wordpress.com/sample-documents/) - still pending on the sample data import templates and [this](http://emerging.commons.gc.cuny.edu/2014/11/collectiveaccess-workflow/)

[Discussion Forum Thread about loading a vocabulary](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/63/load-a-vocabulary) - this may be the only hope, and it’s from 8 years ago.

[Less helpful discussion on loading lists, but whatever](http://collectiveaccess.org/support/forum/index.php?p=/discussion/294513/generating-lists-and-vocabularies-from-imported-dataset)

[Importing the AAT](http://www.collectiveaccess.org/support/forum/?p=/discussion/147/importing-the-aat-thesaurus) - while this is not what we are trying to do, gives an idea of bringing in a more complicated vocabulary.

[Vocabularies](http://docs.collectiveaccess.org/wiki/Vocabularies) - just plain vocabularies

[List & Vocabularies](http://docs.collectiveaccess.org/wiki/Lists_and_Vocabularies) - How to do it in the interface, but nothing like bulk.

[List & Vocabulary Management](http://docs.collectiveaccess.org/wiki/List_and_Vocabulary_Management) - not sure if this is what I need though or not.

[Closest possible discussion thread with example spreadsheets](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/294645/import-mapping-issues) - maybe this?

**More discussions with example spreadsheets:**

[http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/294866/objecthierarchybuilder-refinery-parameters](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/294866/objecthierarchybuilder-refinery-parameters)

[http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/315827/#Comment_315827](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/315827/#Comment_315827)

[http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/295075/list-import/p1](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/295075/list-import/p1)

[http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/315299/#Comment_315299](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/315299/#Comment_315299) (good re: relationships?)

[http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/315230/#Comment_315230](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/315230/#Comment_315230) (same as above?)

[http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/313673/#Comment_313673](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/comment/313673/#Comment_313673) (simple import -> API)

[https://github.com/AmericanNumismaticSociety/ca-tools](https://github.com/AmericanNumismaticSociety/ca-tools)

**Source**

* [Interference Archive Subject Term Mapping Document](https://docs.google.com/spreadsheets/d/11b_0rkUTm6kTfsC81qICYI6TMlJJ_0JZR9hJODwvEr8/edit#gid=0)

* [Collective Access Data Import Mapping Template](https://docs.google.com/spreadsheets/d/1hblyFxv30kL96JN7EWILLayxq1kAyvXAKVNAcG7ZAnw/edit?usp=sharing)

**Things That Are Related But Don’t Make Sense How**

[http://docs.collectiveaccess.org/wiki/Information_Services](http://docs.collectiveaccess.org/wiki/Information_Services)

[http://docs.collectiveaccess.org/wiki/Metadata_Standards](http://docs.collectiveaccess.org/wiki/Metadata_Standards)

### 2. Using Web Service API

[Web Service API](http://docs.collectiveaccess.org/wiki/Web_Service_API)

[Related Web Service API discussion](http://www.collectiveaccess.org/support/forum/index.php?p=/discussion/293482/creating-new-ca-list-items-using-the-web-service-api) 

**Sample usage (for getting)**:

curl -XGET 'https://[user]:[pass]@catalog.interferencearchive.org/admin/service.php/find/ca_objects?q=*&pretty=1'

**Sample usage for creating using [this json](https://github.com/dogrdon/ia-catalog-ingest/blob/master/notes/sample_list_item_ingest.json)**:

curl --upload-file ./new_list_item.json http://[user]:[pass]@45.55.176.103:81/providence_test/service.php/item/ca_list_items

And uploading media (might have to be done with a second pass): [example media upload example json](https://gist.github.com/stefankeidel/1280e7e0864f883b8819)

### Other

**(Updating 1.4 -> 1.5)[http://collectiveaccess.org/support/forum/index.php?p=/discussion/294880/upgrading-providence-from-1-4-to-1-5-1]**

