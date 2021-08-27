import yfinance as yf
import pandas as pd
import csv
from yfinance import shared


file = open("tickers.csv", "r")
csv_reader = csv.reader(file)

def gen_csv():
    for row in csv_reader:
        yield ''.join(row)





load = gen_csv()
list_from_csv = []
for i in load:
    list_from_csv.append(i) 
    tick = yf.Tickers(i)
    a= tick.tickers.keys()
    try:
        ticker_df = tick.history(period='1d')
        print(f"{tick.tickers.keys()} does has downloaded")
    except:
        print(f"{tick.tickers.keys()} does not exist")
        list_from_csv.remove(list(a)[0])
        continue
    print(i)


# keys_to_rm = list(shared._ERRORS.keys())
# keys_to_rm.append('0')


# def gen_stock():
    # a = 0
    # while a < len(keys_to_rm)-1:
        # list_from_csv.remove(keys_to_rm[a])
        # a+=1

df = pd.DataFrame(data=list_from_csv)


df.to_csv('existingtickers.csv', index=False)
