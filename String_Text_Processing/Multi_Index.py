# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:31:00 2022

@author: kanmani
"""
import numpy as np
import pandas as pd
Outer_index=['Group1','Group1','Group1','Group2','Group2','Group2','Group3','Group3','Group3']
Inner_index=['Index1','Index2','Index3','Index1','Index2','Index3','Index1','Index2','Index3']
list(zip(Outer_index,Inner_index))
Hierarchy=list(zip(Outer_index,Inner_index))
Hierarchy=pd.MultiIndex.from_tuples(Hierarchy)
Hierarchy.levels
Hierarchy.codes
R_value=np.random.randint(1,300,45).reshape(9,5)
DF_1=pd.DataFrame(R_value,Hierarchy,columns=['Column1','Column2','Column3','Column4','Column5',])
DF_1['Column1']
DF_1.loc['Group1']
DF_1.loc['Group1'].loc['Index2']
DF_1.index.names=['Groups','Indices']
DF_1.xs('Index1',level='Indices')
