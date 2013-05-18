## Author: D Fehder
## Create Date: 6/23/2011
## Purpose: See mom.org file for details on this project
import re
import os
import csv
import sys
import mparse_util as mp
import logging
import pandas as pd
from collections import defaultdict

path1 = "/home/dcfehder/Dropbox/projects/mom_parser/"
path2 = "/home/dcfehder/Dropbox/projects/mom_parser/proc/"
#file1 = "3021 diet recall 3 25 10.txt"

# this gets the ones that columnsI care about
c= '/home/dcfehder/Dropbox/projects/mom_parser/mparse.sqlite'
ind = mp.load_masterNutrient(c)
ind.append('date')
ind.append('id')
trans = mp.load_matchTable(c)


# this puts them into a series object


# next, you just want to add a column with that series in a DataFrame

holder = []
for file1 in os.listdir(path2):
    print file1
    data_raw = mp.var_extract(path2, file1)
    id1 =mp.sub_id(path2, file1)
    data_dict = mp.translate(data_raw, c)
    data_dict["date"] = mp.sample_date(path2 + file1)
    data_dict["id"] = id1
    series1 = pd.Series(data_dict, index = ind)
    holder.append((id1,series1))

panel_dict = defaultdict(list)
for k, v in holder:
    panel_dict[k].append(v)
    

for key in panel_dict:
    panel_dict[key] = pd.DataFrame(panel_dict[key])
    

outputer = pd.concat(panel_dict)

outputer.to_csv(path1 + "diet_output.csv")

