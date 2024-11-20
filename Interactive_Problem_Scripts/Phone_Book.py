# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:01:18 2022

@author: kanmani
"""

contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}
#get only mailID
name=input('Enter_the_name ')
if name in contacts:
 print(contacts[name][1])
else:
  print('Not found')
  #get number and mailID
name=input('Enter_the_name ')
print(contacts.get(name,'Not found'))
      
