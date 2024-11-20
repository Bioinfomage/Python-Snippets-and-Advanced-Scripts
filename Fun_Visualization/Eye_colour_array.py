# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:42:20 2022

@author: kanmani
"""

data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
a=sum(map(sum,data))

color = input('choose the color')
if color=='brown':
  print(int(31/a*100))
elif color=='blue':
  print(int(43/a*100))
elif color=='green':
        print(int(25/a*100))
elif color=='black':
    print(int(19/a*100))        
