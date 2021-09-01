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

s = ['SAAX', 'SABB', 'SABK', 'SABR', 'SACC', 'SACH', 'SADL', 'SAEC', 'SAFC', 'SAFE', 'SAFM', 'SAFS', 'SAFT', 'SAGD', 'SAGE', 'SAHN', 'SAIA', 'SAIC', 'SAII', 'SAIL', 'SAKH', 'SAKL', 'SALM', 'SALN', 'SAMG', 'SAML', 'SANA', 'SAND', 'SANM', 'SANP', 'SANT', 'SANW', 'SAPX', 'SASN', 'SASR', 'SATC', 'SATS', 'SAVA', 'SAVE', 'SAVW', 'SBAC', 'SBAY', 'SBBA', 'SBBG', 'SBBI', 'SBBP', 'SBCF', 'SBDG', 'SBEA', 'SBES', 'SBET', 'SBEV', 'SBFG', 'SBFM', 'SBGI', 'SBII', 'SBIO', 'SBKK', 'SBKO', 'SBLK', 'SBMC', 'SBNC', 'SBNY', 'SBOW', 'SBOX', 'SBRA', 'SBSI', 'SBSW', 'SBTX', 'SBUG', 'SBUM', 'SBUX', 'SCAL', 'SCAQ', 'SCBS', 'SCBZ', 'SCCB', 'SCCC', 'SCCO', 'SCDA', 'SCDL', 'SCFR', 'SCGX', 'SCGY', 'SCHA', 'SCHB', 'SCHC', 'SCHD', 'SCHE', 'SCHF', 'SCHG', 'SCHH', 'SCHI', 'SCHJ', 'SCHK', 'SCHL', 'SCHM', 'SCHN', 'SCHO', 'SCHP', 'SCHQ', 'SCHR', 'SCHV', 'SCHW', 'SCHX', 'SCHY', 'SCHZ', 'SCIA', 'SCIE', 'SCIF', 'SCKT', 'SCLE', 'SCNA', 'SCND', 'SCNG', 'SCOA', 'SCOB', 'SCON', 'SCOO', 'SCOR', 'SCPE', 'SCPH', 'SCPJ', 'SCPL', 'SCPS', 'SCPT', 'SCRC', 'SCRH', 'SCSC', 'SCSG', 'SCTC', 'SCTN', 'SCTQ', 'SCTY', 'SCVL', 'SCVX', 'SCWO', 'SCWX', 'SCYT', 'SCYX', 'SCZC', 'SDAC', 'SDAD', 'SDCI', 'SDEC', 'SDEF', 'SDEI', 'SDEM', 'SDGA', 'SDGB', 'SDGR', 'SDHY', 'SDIV', 'SDNI', 'SDOG', 'SDON', 'SDOW', 'SDPI', 'SDRC', 'SDSS', 'SDVI', 'SDVY', 'SDWL', 'SEAC', 'SEAH', 'SEAS', 'SEAV', 'SEBC', 'SECI', 'SECO', 'SECT', 'SEDG', 'SEDN', 'SEDO', 'SEED', 'SEEK', 'SEEL', 'SEER', 'SEGI', 'SEIC', 'SEII', 'SEIL', 'SEIX', 'SELB', 'SELF', 'SELR', 'SEMR', 'SENR', 'SENS', 'SENT', 'SEPZ', 'SERA', 'SESI', 'SESN', 'SETO', 'SETY', 'SEVM', 'SEVT', 'SEYE', 'SFBC', 'SFBE', 'SFBI', 'SFBS', 'SFDL', 'SFET', 'SFHD', 'SFHI', 'SFHY', 'SFIG', 'SFIN', 'SFIO', 'SFIV', 'SFIX', 'SFLM', 'SFNC', 'SFOR', 'SFPI', 'SFRI', 'SFRX', 'SFSA', 'SFST', 'SFTW', 'SFUN', 'SFWJ', 'SFYF', 'SFYX', 'SGAM', 'SGBG', 'SGBH', 'SGBI', 'SGBX', 'SGCA', 'SGDH', 'SGDJ', 'SGDM', 'SGEN', 'SGER', 'SGFY', 'SGGC', 'SGHT', 'SGLA', 'SGLB', 'SGLN', 'SGLS', 'SGMA', 'SGMD', 'SGMO', 'SGMS', 'SGNI', 'SGOC', 'SGOL', 'SGOO', 'SGOV', 'SGRB', 'SGRP', 'SGRY', 'SGRZ', 'SGSI', 'SGTB', 'SGTI', 'SGTM', 'SGTN', 'SGTX', 'SGUJ', 'SGYI', 'SHAC', 'SHAG', 'SHAK', 'SHBI', 'SHCC', 'SHCR', 'SHDC', 'SHEN', 'SHFT', 'SHGP', 'SHGY', 'SHIP', 'SHLD', 'SHLS', 'SHLX', 'SHMN', 'SHMP', 'SHNL', 'SHOM', 'SHOO', 'SHOP', 'SHPS', 'SHQA', 'SHRG', 'SHSP', 'SHUS', 'SHWK', 'SHWZ', 'SHYD', 'SHYF', 'SHYG', 'SHYL', 'SIAF', 'SIBC', 'SIBE', 'SIBN', 'SIEB', 'SIEN', 'SIFY', 'SIGA', 'SIGI', 'SIGL', 'SIGN', 'SIGO', 'SIGY', 'SIHC', 'SIII', 'SILC', 'SILJ', 'SILK', 'SILO', 'SILS', 'SILV', 'SILX', 'SIMA', 'SIMC', 'SIMO', 'SIMP', 'SIMS', 'SINC', 'SING', 'SINO', 'SINT', 'SINV', 'SINX', 'SIOX', 'SIPC', 'SIPN', 'SIRC', 'SIRI', 'SIRR', 'SITC', 'SITE', 'SITM', 'SITS', 'SIVB', 'SIVE', 'SIVR', 'SIXA', 'SIXD', 'SIXH', 'SIXL', 'SIXN', 'SIXS', 'SIZE', 'SJIJ', 'SJIV', 'SJNK', 'SKAS', 'SKFG', 'SKGO', 'SKIL', 'SKIN', 'SKKY', 'SKLV', 'SKLZ', 'SKOR', 'SKPI', 'SKPN', 'SKPO', 'SKRJ', 'SKRV', 'SKSK', 'SKTO', 'SKTP', 'SKVI', 'SKVY', 'SKWG', 'SKYA', 'SKYE', 'SKYF', 'SKYI', 'SKYT', 'SKYU', 'SKYW', 'SKYY', 'SLAB', 'SLAC', 'SLAM', 'SLBG', 'SLCA', 'SLCH', 'SLCO', 'SLCR', 'SLCT', 'SLDB', 'SLDX', 'SLGD', 'SLGG', 'SLGL', 'SLGN', 'SLHG', 'SLJB', 'SLLN', 'SLNG', 'SLNK', 'SLNM', 'SLNO', 'SLNX', 'SLOT', 'SLQD', 'SLQT', 'SLRC', 'SLRK', 'SLRX', 'SLSR', 'SLTN', 'SLTZ', 'SLUP', 'SLVO', 'SLVP', 'SLYG', 'SLYV', 'SMAA', 'SMAL', 'SMAR', 'SMAS', 'SMBC', 'SMBK']

df = pd.DataFrame(data=s)
df.to_csv('JSONstocks/S.csv', index=False, header=False)