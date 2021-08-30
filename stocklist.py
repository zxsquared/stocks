"""
Copyright 2021 Magnus Peterson-Munoz

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import yfinance as yf
import csv
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--l", type=str, action="store", help="The the letter for which CSV you use", default=None)

csv_letter = ""
args = parser.parse_args()
if args.l:
    csv_letter = args.l

print(csv_letter)


file = open(f"LetterTickers/{csv_letter.upper()}.csv", "r")
csv_reader = csv.reader(file)
def gen_csv():
    for row in csv_reader:
        yield ''.join(row)
keys_to_add = []
load = gen_csv()
for i in load:
    tick = yf.Ticker(i)
    ticker_df = tick.history()
    try:
        if ticker_df.empty == False:
            keys_to_add.append(i)    
    except:
        continue
print(keys_to_add)
df = pd.DataFrame(data=keys_to_add)
df.to_csv(f'JSONstocks/{csv_letter.upper()}.csv', index=False, header=False)
