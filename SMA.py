import pandas as pd
import numpy as np

#For reading the contents of csv file
df = pd.read_csv('RELIANCE.csv')

#Selecting the columns required for SMA calculation
df = df[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

df['Date']=df['Date']

#Calculating SMA using rolling
df['SMA(Open) 10D'] = df['Open'].rolling(window=10, min_periods=1).mean()
df['SMA(High) 10D'] = df['High'].rolling(window=10, min_periods=1).mean()
df['SMA(Low) 10D'] = df['Low'].rolling(window=10, min_periods=1).mean()
df['SMA(Close) 10D'] = df['Close'].rolling(window=10, min_periods=1).mean()
df['SMA(Adj Close) 10D'] = df['Adj Close'].rolling(window=10, min_periods=1).mean()
df['SMA(Volume) 10D'] = df['Volume'].rolling(window=10, min_periods=1).mean()

#Since the window size is 10, SMA of first 9 elements must be NAN
df.iloc[:9, 7:] = np.nan

# Assign NaN values for SMA for those input is NAN
df.loc[df['Open'].isna(), 'SMA(Open) 10D'] = np.nan
df.loc[df['High'].isna(), 'SMA(High) 10D'] = np.nan
df.loc[df['Low'].isna(), 'SMA(Low) 10D'] = np.nan
df.loc[df['Close'].isna(), 'SMA(Close) 10D'] = np.nan
df.loc[df['Adj Close'].isna(), 'SMA(Adj Close) 10D'] = np.nan
df.loc[df['Volume'].isna(), 'SMA(Volume) 10D'] = np.nan

df=df.round(6)

# For saving the SMA values to a CSV file
df.to_csv('RELIANCE.csv',index=False)

print("Updated RELIANCE.csv file")

