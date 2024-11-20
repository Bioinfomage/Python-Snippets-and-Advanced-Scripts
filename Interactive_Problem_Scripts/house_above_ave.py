# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:14:33 2022

@author: kanmani
"""

prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
#your code goes here
ave=sum(prices)/len(prices)
print(ave)
Above_ave=0
for n in prices:
    if n>ave:
     Above_ave=Above_ave+1
print(Above_ave)     
 
       
    