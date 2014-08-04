# get a list of packages with Github as a homepage

import pickle
import xmlrpclib
import pprint
client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')



with open('python2only','r') as f:

    py2onlylist = pickle.load(f)




#print len(py2onlylist)
py2onlylist = list(py2onlylist)

py2gitlist =[]

#print py2onlylist[0] 

for i in py2onlylist:
    rel = client.package_releases(i)
    if rel:
        link = client.release_data(i,rel[0])["home_page"]
        if "github" in link:
            py2gitlist.append(link)
            print link

with open('python2gitlist','w') as f:
    pickle.dump(py2gitlist,f)
