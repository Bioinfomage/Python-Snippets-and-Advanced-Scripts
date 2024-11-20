# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:00:32 2022

@author: kanmani
"""

#def sum(x):
#    for i in range(x):
#     print(i)
#    return
#print(sum(10))
#to find particular word in a text-search engine!    
text=input()
word=input()
def search(text,word):
   if(text.count(word)>=1):
       print('Word found')
   else:
       print('Word not found')
search(text,word)        