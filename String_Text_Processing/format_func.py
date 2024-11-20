# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:57:48 2022

@author: kanmani
"""
#format
print("{0}{1}{0}".format("abra","cad"))

#split
x='my home'
words=x.split(' ')
res=words[1]
print(res)

#replace
x='hello world'
print(x.replace('world','me'))
y='Hi all!good morning!hope you are all doing well!'
print(y.replace('!','!!',2))