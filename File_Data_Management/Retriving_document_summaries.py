# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:08:46 2024

@author: kanmani
"""

from Bio import Entrez
Entrez.email = 'kanmanimr.biotech@gmail.com'
record = Entrez.read(Entrez.esearch(db = 'pmc', term ='biopython', retmax=2000)) #retmax comment is for setting retriving limit
print(type(record))                                                                                                                                                                 
print(record.keys())
for key in record.keys():
    print(key, ":", record [key])
biopythonID = record ["IdList"]
# print(biopythonID)

#retriving specified details from biopythonID

for ID in biopythonID[:2]: #only limited first 1 id
    summary = Entrez.read(Entrez.esummary(db='pmc', id=ID))
    #print(type(summary))#to know the type to retrive data, here its list
    
    for handle in summary:
        #print(type(handle))
        #print(handle)#to print all the keys in handle, in next step we can select specified keys
        print(handle['Id'], '\t', handle['Title'], '/t', handle['DOI'])