# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:32:30 2022

@author: kanmani
"""

import numpy as np
test_array=np.array([[1,2,3],[4,5,9],[6,7,8]])
print(test_array)
print(test_array.ndim)
print(test_array.shape)
print(test_array.size)
print(test_array[2,1])
print(type(test_array))
for i in test_array:
    print(i)
for i in test_array.flat:
    print(i)
for i in test_array.flat:
    print(i,end=" ")
np.zeros(6)
np.zeros((6,3))
np.ones((2,4))
np.ones((2,4),dtype=int)
np.ones((2,4),dtype=float)
np.full((3,3),5)
np.full((3,3),5,dtype=float)
np.arange(0,20)
np.arange(0,20).reshape(4,5)
np.arange(30,20,-2)
np.linspace(0,10)
np.linspace(0,10,5)
np.random.randint(10,20,8)
np.random.randint(10,20,8).reshape(2,4)
x=np.random.randint(0,100,10)
x.sum()
x.max()
x.min()
x.std()
x.mean()
np.eye(2,3)
np.empty(2)
np.empty((2,3))
np.identity(3)