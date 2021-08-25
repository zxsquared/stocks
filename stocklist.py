import yfinance as yf
import pandas as pd
import csv
from yfinance import shared

file = open("tickers.csv", "r")
csv_reader = csv.reader(file)

list_from_csv = []
for row in csv_reader:
    list_from_csv.append(''.join(row))

tick = yf.Tickers(list_from_csv)

ticker_df = tick.history(period='1d')

keys_to_rm = list(shared._ERRORS.keys())
keys_to_rm.append('0')

a = 0
while a < len(keys_to_rm)-1:
    for c in range(len(keys_to_rm)-1):
        list_from_csv.remove(keys_to_rm[a])
        a+=1

df = pd.DataFrame(data=list_from_csv)


df.to_csv('existingtickers.csv', index=False)