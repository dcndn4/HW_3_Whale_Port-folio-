# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 08:10:50 2021

@author: CS_Knit_tinK_SC
"""

import pandas as pd
import numpy as np
from pathlib import Path
%matplotlib inline
#%%

portfolio_a_std = np.random.normal(scale=0.5, size=10000)
portfolio_b_std = np.random.normal(scale=1.0, size=10000)
portfolio_c_std = np.random.normal(scale=1.5, size=10000)

portfolio_std = pd.DataFrame({
    "0.5": portfolio_a_std,
    "1.0": portfolio_b_std,
    "1.5": portfolio_c_std
})

portfolio_std.plot.hist(stacked=True, bins=100)

#%%
