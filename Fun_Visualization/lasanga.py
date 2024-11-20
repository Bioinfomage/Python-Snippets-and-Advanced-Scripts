# -*- coding: utf-8 -*-
"""
Created on Thu May  5 23:27:55 2022

@author: kanmani
"""

#remaining baking time
def bake_time_remaining(EXPECTED_BAKE_TIME,elapsed_time):
    b=EXPECTED_BAKE_TIME-elapsed_time
    return ('Bake time remaining',b)
#preparation time # total elapsed  time    
def elapsed_time_in_minutes(elapsed_time,PREPARATION_TIME):
    a=elapsed_time+PREPARATION_TIME
    print ('total elapsed time',a)
    return a
#user input    
EXPECTED_BAKE_TIME=40
print("EXPECTED_BAKE_TIME",EXPECTED_BAKE_TIME)
elapsed_time=int(input('Elapsed time '))
bake_time_remaining(EXPECTED_BAKE_TIME,elapsed_time)
layer=int(input("Number of Layers "))
PREPARATION_TIME=2*layer
print('PREPARATION_TIME',PREPARATION_TIME)
elapsed_time_in_minutes(elapsed_time,PREPARATION_TIME)