# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:36:36 2022

@author: kanmani
"""

import numpy as np
Array_1=np.random.randint(5,30,10)
print(Array_1)
Array_1[2:6]#2 to 6 th element
Array_1[:6]#till 6th element
Array_1[:5]=5#replace intgrs as 5 till 5th element
slic=np.random.randint(0,100,20).reshape(5,4)# reshape 5 rows 4 columns
slic[2:4]#2 to 4 th row
slic[:4]#till 4th row
slic[3,2]#single element
slic[:,2:4]#2 to 4rth column
slic[:,(2,3)]#2 to 4rth column
#view()- this comment 
Array_cpy=np.arange(0,15).reshape(3,5)
Array_cpy_sc=Array_cpy.view()#original reflect changes
Array_cpy[0,3]*=2
Array_cpy_dc=Array_cpy.copy()#original doesnt reflects changes
random_element=Array_1[np.random.randint(0,8)]#random element by choosing index
index_value=np.where(Array_1==random_element)#to know index value of random element
#pad Array
Array_pad=np.random.randint(0,100,15).reshape(5,3)
Array_pad=np.pad(Array_pad,pad_width=1,mode="constant",constant_values=0)
Array_pad.sort()#row wise sorting
#random element replacing
rand_replc_array=np.random.randint(0,50,20).reshape(5,4)
rand_replc_array=np.put(rand_replc_array,np.random.choice(range(4,5),replace=False),1)
#reshape and slice
array_5=np.random.randint(0,101,100).reshape(10,10)
array_5.sort()
array_5[4:,5:]#slicing from 4rth row's 5th element
array_5[2:4,5:7]#slicing result gives R2,R3 and C5,C6 elements
array_5[:,8]#results 8th column alone
array_5[8,:]#results 8th row alone
array_5[8:]#results 8 and 9th rows
Array_A=((np.random.rand(15)*10).astype(int)).reshape(3,5)#results 3*5 array withrandom 15 numbers from 0 t0 10
Array_B=((np.random.rand(15)*10).astype(int)).reshape(3,5)