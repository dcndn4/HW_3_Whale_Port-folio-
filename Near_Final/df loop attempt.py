# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:45:05 2021

@author: CS_Knit_tinK_SC
"""

import pandas as pd
import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])

ser = pd.Series(data, index =[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

print(ser.iloc[[0]])

#%%

for item in ser.iloc[0]:
    if item == 12:
        print(ser.iloc[1])
    else:
        print(ser.iloc[[0]])

