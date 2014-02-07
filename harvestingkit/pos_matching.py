import os
from invenio.invenio_connector import InvenioConnector

inspire = InvenioConnector("http://inspirehep.net/")

file_path = [(files[0],paths) for paths,dirs,files in os.walk("/home/georgios/Documents/pos") if files]
matched_records = []
unmatched_records = []

for f,p in file_path:
	#print f
	f = f.split(".")[0]
	p = "/afs/cern.ch/project/inspire/" + p[25:]
	conference = f.split("_")[0].replace(" ","")
	proceeding = ""
	try:
		proceeding = f.split("_")[1]
	except IndexError:
		print f
	recid = ""
	query = "773__p:pos 773__v:%s 773__c:%s" % (conference,proceeding)
	results = inspire.search(p=query)
	if results:
		matched_records.append((results[0]["001__"][0],os.path.join(p,f)+".pdf"))
	else:
		unmatched_records.append(os.path.join(p,f)+".pdf")

matched = open('matched.txt','w')
matched.write("\n".join(["%s---%s"%(f,rec) for rec,f in matched_records]))
matched.close()
unmatched = open('unmatched.txt','w')
unmatched.write("\n".join(unmatched_records))
unmatched.close()
