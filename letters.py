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

b = ['BABA', 'BABB', 'BABL', 'BAFI', 'BALT', 'BALY', 'BAMH', 'BAMI', 'BAMR', 'BANC', 'BAND', 'BANF', 'BANI', 'BANR', 'BANT', 'BANX', 'BAOB', 'BAOS', 'BAPR', 'BARK', 'BASA', 'BASE', 'BATL', 'BATT', 'BAUG', 'BAYP', 'BBAR', 'BBAX', 'BBBT', 'BBBY', 'BBCA', 'BBCP', 'BBDA', 'BBDC', 'BBDO', 'BBEU', 'BBGI', 'BBIG', 'BBIN', 'BBIO', 'BBJP', 'BBLR', 'BBMC', 'BBME', 'BBRE', 'BBRW', 'BBSA', 'BBSC', 'BBSI', 'BBUS', 'BBVA', 'BBWI', 'BCAB', 'BCAC', 'BCAL', 'BCAP', 'BCAT', 'BCBF', 'BCBP', 'BCCI', 'BCDA', 'BCEI', 'BCEL', 'BCHG', 'BCII', 'BCLI', 'BCML', 'BCND', 'BCOR', 'BCOV', 'BCOW', 'BCPC', 'BCRX', 'BCSF', 'BCTF', 'BCTX', 'BCYC', 'BCYP', 'BDCM', 'BDCO', 'BDCX', 'BDCZ', 'BDEC', 'BDGR', 'BDPT', 'BDRY', 'BDSI', 'BDSX', 'BDTX', 'BDVB', 'BDXB', 'BEAG', 'BEAM', 'BEBE', 'BECN', 'BECO', 'BEDU', 'BEDZ', 'BEEM', 'BEEN', 'BEGI', 'BEHL', 'BEKE', 'BELP', 'BENE', 'BEPC', 'BEPH', 'BERI', 'BERK', 'BERY', 'BERZ', 'BEST', 'BETZ', 'BEUT', 'BFAM', 'BFCC', 'BFCH', 'BFDE', 'BFEB', 'BFIN', 'BFIT', 'BFLY', 'BFNH', 'BFOR', 'BFRA', 'BFST', 'BFTR', 'BGCP', 'BGEM', 'BGFV', 'BGIO', 'BGLC', 'BGLD', 'BGMD', 'BGNE', 'BGRN', 'BGRP', 'BGRY', 'BGSF', 'BGSX', 'BHAT', 'BHLB', 'BHLL', 'BHPA', 'BHRB', 'BHSE', 'BHTG', 'BHVN', 'BIBL', 'BICB', 'BICK', 'BIDU', 'BIEI', 'BIEL', 'BIGC', 'BIGY', 'BIGZ', 'BIIB', 'BIIO', 'BILI', 'BILL', 'BILS', 'BIMI', 'BIOC', 'BIOF', 'BIOL', 'BIOT', 'BIOX', 'BIPC', 'BIPH', 'BITE', 'BITF', 'BITQ', 'BITW', 'BIVI', 'BIZD', 'BJAN', 'BJRI', 'BJUL', 'BJUN', 'BKAG', 'BKCC', 'BKCH', 'BKEN', 'BKEP', 'BKHY', 'BKIE', 'BKIT', 'BKLC', 'BKLN', 'BKMC', 'BKMM', 'BKMP', 'BKNG', 'BKRP', 'BKSB', 'BKSC', 'BKSD', 'BKSE', 'BKTI', 'BKUH', 'BKUI', 'BKYI', 'BLBD', 'BLCM', 'BLCN', 'BLCT', 'BLDE', 'BLDG', 'BLDP', 'BLDR', 'BLDV', 'BLEG', 'BLES', 'BLFE', 'BLFR', 'BLFS', 'BLFY', 'BLGI', 'BLGO', 'BLHY', 'BLIN', 'BLKB', 'BLLB', 'BLMC', 'BLMN', 'BLMS', 'BLND', 'BLNK', 'BLOK', 'BLPG', 'BLPH', 'BLRX', 'BLSA', 'BLSP', 'BLTS', 'BLUA', 'BLUE', 'BLUU', 'BLUW', 'BLXX', 'BMAR', 'BMAY', 'BMBL', 'BMBN', 'BMCS', 'BMEA', 'BMED', 'BMEZ', 'BMIN', 'BMIX', 'BMMJ', 'BMNM', 'BMRA', 'BMRC', 'BMRK', 'BMRN', 'BMTC', 'BMTM', 'BMTX', 'BMXC', 'BMXI', 'BNDC', 'BNDW', 'BNDX', 'BNED', 'BNET', 'BNFT', 'BNGO', 'BNKD', 'BNKU', 'BNOV', 'BNOW', 'BNSO', 'BNTC', 'BNTX', 'BNXR', 'BOAC', 'BOAS', 'BOAT', 'BOCH', 'BOCT', 'BODY', 'BOGN', 'BOID', 'BOIL', 'BOKF', 'BOLT', 'BOMH', 'BOMN', 'BOND', 'BONZ', 'BOOM', 'BOOT', 'BOPO', 'BORK', 'BORR', 'BORT', 'BOSC', 'BOSS', 'BOTJ', 'BOTX', 'BOTY', 'BOTZ', 'BOUT', 'BOWX', 'BOXL', 'BOXS', 'BPCP', 'BPMC', 'BPMP', 'BPOP', 'BPRN', 'BPSR', 'BPTH', 'BPTS', 'BRAG', 'BRAV', 'BRBL', 'BRBR', 'BRBS', 'BRBW', 'BRCN', 'BRDG', 'BRER', 'BREZ', 'BRFH', 'BRFS', 'BRGC', 'BRGO', 'BRID', 'BRIV', 'BRKL', 'BRKR', 'BRKS', 'BRLI', 'BRLL', 'BRMK', 'BRNE', 'BROE', 'BROG', 'BRPM', 'BRQS', 'BRRN', 'BRSE', 'BRSF', 'BRSI', 'BRSP', 'BRST', 'BRTI', 'BRTX', 'BRVO', 'BRYN', 'BRZL', 'BRZU', 'BRZV', 'BSAC', 'BSAE', 'BSBE', 'BSBK', 'BSBR', 'BSCA', 'BSCE', 'BSCL', 'BSCM', 'BSCN', 'BSCO', 'BSCP', 'BSCQ', 'BSCR', 'BSCS', 'BSCT', 'BSCU', 'BSDE', 'BSEG', 'BSEP', 'BSET', 'BSGA', 'BSGC', 'BSGM', 'BSHI', 'BSIG', 'BSJL', 'BSJM', 'BSJN', 'BSJO', 'BSJP', 'BSJQ', 'BSJR', 'BSJS', 'BSML', 'BSMM', 'BSMN', 'BSMO', 'BSMP', 'BSMQ', 'BSMR', 'BSMS', 'BSMT', 'BSMU', 'BSMX', 'BSND', 'BSPK', 'BSPM', 'BSPR', 'BSQR', 'BSRR', 'BSSP', 'BSTG', 'BSTK', 'BSTO', 'BSTZ', 'BSVN', 'BSYI', 'BTAI', 'BTAL', 'BTAQ', 'BTBT', 'BTCM', 'BTCY', 'BTDG', 'BTEC', 'BTEK', 'BTGN', 'BTIM', 'BTLN', 'BTNB', 'BTRS', 'BTTR', 'BTWN', 'BTZI', 'BUDZ', 'BUFD', 'BUFF', 'BUFR', 'BUKS', 'BULZ', 'BUNM', 'BURL', 'BUSE', 'BUYZ', 'BUZZ', 'BVFL', 'BVXV', 'BWAC', 'BWAY', 'BWEL', 'BWEN', 'BWFG', 'BWMG', 'BWMN', 'BWMX', 'BWPC', 'BWSN', 'BWTL', 'BWVI', 'BWXT', 'BXLC', 'BXMT', 'BXMX', 'BXNG', 'BXRX', 'BXXY', 'BYFC', 'BYLB', 'BYLD', 'BYND', 'BYOC', 'BYRG', 'BYRN', 'BYSD', 'BYSI', 'BYTS', 'BZIC', 'BZRD', 'BZRT', 'BZTG', 'BZUN', 'BZWR', 'BZYR']


df = pd.DataFrame(data=b)
df.to_csv('JSONstocks/B.csv', index=False, header=False)