# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:23:05 2022

@author: kanmani
"""

text = input()
l=text.split(" ")
T=0
for i in(l):
 T=T+int(len(i))
print(T/len(l))
