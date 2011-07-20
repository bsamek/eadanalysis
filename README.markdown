EAD Analysis
============

ead.py contains two scripts for a simple analysis of EAD files.
save\_comments(directory, comments\_file) saves
all comments in a _directory_ of EAD documents to a _file_.
count\_files\_containing\_tag(tag, directory) counts how many files in a
_directory_ contain a _tag_. 

Notes
-----
There are 14 files which are encoded in utf-16. ead.py chokes on them:

* EMF.xml
* CS.xml
* KCGB.xml
* FLM.xml
* ANLM.xml
* KCAC.xml
* JMK.xml
* BLM.xml
* AG.xml
* JRNS.xml
* AMT.xml
* EFB.xml
* BRA.xml
* KCAS.xml

Also, there is one HTML file amont the XML files, aaa-00109.html.
