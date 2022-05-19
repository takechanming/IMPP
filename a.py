from pandas_datareader.stooq import StooqDailyReader
import datetime as dt
import pandas as pd
import pickle as pk

start = dt.date(2006, 11, 12)
end = dt.date(2022, 5, 12)
brand = '^NKX'
stooq = StooqDailyReader(brand, start, end)
data = stooq.read()
data.to_pickle('/content/drive/MyDrive/IMPP/Data/'+ brand + '.pkl')

start = dt.date(2006, 11, 12)
end = dt.date(2022, 5, 12)
brand = '4528.JP'
stooq = StooqDailyReader(brand, start, end)
data = stooq.read()
data.to_pickle('/content/drive/MyDrive/IMPP/Data/'+ brand + '.pkl')

start = dt.date(2006, 11, 12)
end = dt.date(2022, 5, 12)
brand = '^TPX'
stooq = StooqDailyReader(brand, start, end)
data = stooq.read()
data.to_pickle('/content/drive/MyDrive/IMPP/Data/'+ brand + '.pkl')
