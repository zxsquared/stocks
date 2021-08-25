import yfinance as yf
import pandas as pd
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--s", type=str, action="store", help="The start date of your stocks", default="2021-01-01")

parser.add_argument("--e", type=str, action="store", help="The end date of your stocks", default="2021-02-01")

sstart = ""
send = ""


args = parser.parse_args()
if args.s:
    sstart = args.s
if args.e:
    send = args.e


print(sstart)
print(send)

ticker_data = ""
question = input("Type in a stock ticker to get data from the time period you have set: ").upper()
print(question)
 
if re.search(' ', question):
    ticker_data = yf.Tickers(question)
else:
    ticker_data = yf.Ticker(question)


ticker_df = ticker_data.history(period='1d', start=sstart, end=send)

if ticker_df.empty == True:
    raise AttributeError("Bad stock, please try again!")
else:
    print(ticker_df)
    ticker_df.to_csv(rf'CSVStock/{question.upper()}-{send}_stock.csv', index=True, header=True)
