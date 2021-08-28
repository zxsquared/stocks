"""
PLEASE DO NOT RUN THIS FILE!!!
You will immediately remove all progress

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

from string import ascii_uppercase
import pandas as pd


for i in ascii_uppercase:
    df = pd.DataFrame()
    df.to_csv(f'LetterTickers/{i}.csv', index=False, header=False)