"""
Copyright (c) 2021 Magnus Peterson-Munoz

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

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
