# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:51:55 2021

@author: CS_Knit_tinK_SC
"""

# Initial imports
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

%matplotlib inline


#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_w = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/whale_returns.csv"
whale_returns = pd.read_csv(
    csv_path_w, parse_dates=True, index_col="Date", infer_datetime_format=True
)
print(whale_returns.head())

#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_a = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/algo_returns.csv"
algo_returns = pd.read_csv(
    csv_path_a, parse_dates=True, index_col="Date", infer_datetime_format=True
)
print(algo_returns.head())

#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_s = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/sp500_history.csv"
#sp500_history = pd.read_csv(
#csv_path_s, parse_dates=True, index_col="Date", infer_datetime_format=True
#)
sp500_history = pd.read_csv(csv_path_s)
print(sp500_history.head())

#%%

# Check Data Types
print(sp500_history.dtypes)

#%%

#Set index as date field

#sp500_history.set_index(sp500_history['Date'], inplace=True)
#print(sp500_history.head())

sp500_history.set_index(pd.to_datetime(sp500_history['Date'], infer_datetime_format=True), inplace=True)
print(sp500_history.head())

#%%
# Drop the extra date column
sp500_history.drop(columns=['Date'], inplace=True)
print(sp500_history.head())

#%%

