# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:14 2022

@author: kanmani
"""
#insert&remove
x=[2,4,8,9,5]
x.insert(1,3)
x.remove(9)
x.insert(0,x.count(8))
print(x[3])

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

z='hello'
print(max(z))