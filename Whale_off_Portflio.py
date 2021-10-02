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

# whale df is 1060/4
print(whale_returns.head())
#%%

# Count nulls
print(whale_returns.isnull().mean() * 100)

#%%

whale_returns=whale_returns.dropna()


#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_a = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/algo_returns.csv"
algo_returns = pd.read_csv(
    csv_path_a, parse_dates=True, index_col="Date", infer_datetime_format=True
)

# algo df is 1241/2
print(algo_returns.head())

#%%

# Count nulls
print(algo_returns.isnull().mean() * 100)

#%%

algo_returns=algo_returns.dropna()

#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_s = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/sp500_history.csv"
#sp500_history = pd.read_csv(
#csv_path_s, parse_dates=True, index_col="Date", infer_datetime_format=True
#)
sp500_history = pd.read_csv(csv_path_s)

# sp500 is 1649/2
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
print(sp500_history.dtypes)
#%%

sp500_history=sp500_history.dropna()

#%%

sp500_history['Close'] = sp500_history['Close'].str.replace('$','')

#%%

sp500_history['Close']=sp500_history['Close'].astype('float')

#%%

sp500_returns = sp500_history.pct_change()

#%%

sp500_returns.columns = ["SP500"] 

#%%

all_returns = pd.concat([algo_returns, whale_returns, sp500_returns], axis='columns', join = 'inner')

#%%

# Plot daily returns of all portfolios
algo_returns.plot()
whale_returns.plot()
sp500_returns.plot()

#%%

cumulative_algo_returns = (1 + algo_returns).cumprod() - 1
cumulative_whale_returns = (1 + whale_returns).cumprod() - 1
cumulative_sp500_returns = (1 + sp500_returns).cumprod() - 1

#%%

cumulative_algo_returns.plot()
cumulative_whale_returns.plot()
cumulative_sp500_returns.plot()

