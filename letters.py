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

x = ['XAIR', 'XALL', 'XBAP', 'XBIO', 'XBIT', 'XBJL', 'XBOR', 'XBUY', 'XCAN', 'XCEM', 'XCLL', 'XCLR', 'XCPL', 'XCPT', 'XCRP', 'XCRT', 'XCUR', 'XDAP', 'XDAT', 'XDIV', 'XDJL', 'XDQQ', 'XDSL', 'XDSQ', 'XELA', 'XELB', 'XENE', 'XENO', 'XENT', 'XERI', 'XERS', 'XFCH', 'XFLS', 'XFLT', 'XFOR', 'XFTB', 'XITK', 'XITO', 'XJUN', 'XKCP', 'XKFF', 'XKFS', 'XKII', 'XKST', 'XLNX', 'XLPI', 'XLRE', 'XLRM', 'XLRN', 'XLSR', 'XLTD', 'XLWH', 'XMEX', 'XMHQ', 'XMLV', 'XMMO', 'XMPT', 'XMSW', 'XMTR', 'XMVM', 'XNCR', 'XNDA', 'XNET', 'XNTK', 'XOMA', 'XONE', 'XOUT', 'XPDI', 'XPEL', 'XPER', 'XPEV', 'XPND', 'XPOA', 'XPOF', 'XRAY', 'XREG', 'XRLV', 'XRMI', 'XRXH', 'XSHD', 'XSHQ', 'XSLV', 'XSMO', 'XSNX', 'XSOE', 'XSPA', 'XSPT', 'XSVM', 'XSVT', 'XTAP', 'XTEG', 'XTJL', 'XTLB', 'XTMM', 'XTNT', 'XTPT', 'XTRM', 'XVOL', 'XWEB']
df = pd.DataFrame(data=x)
df.to_csv('JSONstocks/X.csv', index=False, header=False)