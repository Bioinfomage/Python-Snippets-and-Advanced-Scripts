# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 22:15:24 2022

@author: kanmani
"""

import numpy as np
import pandas as pd
pd_series=pd.Series([5,3,8,2,7])
pd_series_2=pd.Series(25,range(10))
pd_series[3]
p_Random=pd.Series(np.random.randint(1,80,20))# we can't assign direct random in pandas
p_Random.describe()#max,min,std,count,etc
p_Random.head()#we can custom number in parenthesis
p_Random.tail()#we can custom number in parenthesis
P_series_2=pd.Series([2,9,4,1,0],index=['kanz','nila','tamil','rani','raana'])
P_series_2.nila
P_series_2['kanz']
P_series_D=pd.Series({'one':1,'two':2,'three':3})
P_series_5=pd.Series(['one','two','three'])
P_series_5.str.contains('o')
P_series_5.str.upper()
Data=[2,6,4,8]
Label=['apple','kiwi','jack','mango']
pd.Series(data=Data,index=Label)
list_1=pd.Series([5,5,8],['bricks','cement','sand'])
list_2=pd.Series([5,6,8,2],['bricks','cement','sand','steel'])
list_1+list_2