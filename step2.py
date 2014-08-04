# Take two pickles, extract the sets and dump out pickle object with the difference of the two sets

import pickle

with open('python2','r') as f:

    py2list = pickle.load(f)



with open('python3','r') as f:

    py3list = pickle.load(f)


p2set = set([])

for i in py2list:
    print "list len: ", len(i)
    print "set len: ", len(set(i))
    p2set.update(i)
    

p3set = set([])

for i in py3list:
    print "list len: ", len(i)
    print "set len: ", len(set(i))
    p3set.update(i)


print len(p2set),len(p3set)

p2onlyset = p2set.difference(p3set)

print len(p2onlyset)


with open('python2only','w') as f:
    pickle.dump(p2onlyset,f)
