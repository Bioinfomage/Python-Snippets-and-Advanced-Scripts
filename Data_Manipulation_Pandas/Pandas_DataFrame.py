# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:45:31 2022

@author: kanmani
"""


import numpy as np
import pandas as pd
list_dict={'Midcap_stock':[8,6,4],'Bluechip_stock':[5,7,5],'Smallcap_stock':[53,51,6]}
dataframe1=pd.DataFrame(list_dict)
dataframe1=pd.DataFrame(list_dict,index=['Jan','Feb','Mar'])
dataframe1.Bluechip_stock
dataframe1['Smallcap_stock']
dataframe1.loc['Jan']
dataframe1.iloc[1]
dataframe1.loc['Jan':'Mar',['Midcap_stock','Smallcap_stock']]
dataframe1[dataframe1>5]
dataframe1[(dataframe1>5)&(dataframe1>10)]
dataframe1[(dataframe1>5)|(dataframe1>10)]
dataframe1.at['Jan','Midcap_stock']
dataframe1.iat[0,2]
#To replace data
dataframe1.at['Jan','Midcap_stock']=48
dataframe1.iat[0,2]=3
dataframe1.describe()
pd.set_option('precision',2)
dataframe1.mean()
dataframe1.T#Transpose
dataframe1.T.describe()
dataframe1.sort_index(ascending=False)
dataframe1.sort_index(ascending=True)
dataframe1.sort_index(axis=1)
dataframe1.sort_index(axis=0)
