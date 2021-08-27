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

from json.decoder import JSONDecodeError
import yfinance as yf
import csv
import pandas as pd
from yfinance import shared

file = open("tickers.csv", "r")
csv_reader = csv.reader(file)

def gen_csv():
    for row in csv_reader:
        yield ''.join(row)




keys_to_rm = []
load = gen_csv()
for i in load:
    tick = yf.Ticker(i)
    ticker_df = tick.history()
    try:
        if ticker_df.empty:
            keys_to_rm = list(shared._ERRORS.keys())
    except JSONDecodeError:
        continue


df = pd.DataFrame(data=keys_to_rm)

df.to_csv('JSONstocks/keys_to_rm.csv', index=False, header=False)