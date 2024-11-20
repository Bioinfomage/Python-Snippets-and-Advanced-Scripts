# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:15:39 2022

@author: kanmani
"""

import numpy as np
import pandas as pd
Dict={'kite':[5,7,9],'thread':[5,9,4],'gum':[8,5,3]}
PD_frames=pd.DataFrame(Dict,index=['row1','row2','row3'])
PD_frames['stick']=[4,3,2]#Add column
#to add new row case 1
N_row={'kite':2,'thread':3,'gum':8,'stick':6}
PD_frames=PD_frames.append(N_row,ignore_index=True)
#to add new row case 2
n_R2=pd.Series(data={'kite':1,'thread':9,'gum':6,'stick':4},name='row4')
PD_frames=PD_frames.append(n_R2,ignore_index=False)
PD_frames.pop('thread')#delete single column
PD_frames.drop(['gum','stick'],axis=1)#delete multiple column
PD_frames.drop(['row4'],axis=0)#to delete row

import numpy as np
import pandas as pd
dict3={'a':[5,6,4,1,4,9],
      'b':[4,9,2,4,5,7],
      'c':[7,5,6,2,1,4],
      'd':[3,8,1,6,7,4],
      'f':[2,8,4,3,7,1],
      'g':[9,3,8,2,4,8]}
PD_DF6=pd.DataFrame(dict3,index=['Day1','Day2','Day3','Day4','Day5','Day6'])
PD_DF6.insert(4,'e',[5,6,2,1,4,7])#insert
PD_DF6.head(4)
PD_DF6.tail(4)
PD_DF6['c']+=2#basic math operation
PD_DF6['c'].value_counts()#no of presence of elements