## Author: D Fehder
## Create Date: 6/23/2011
## Purpose: See mom.org file for details on this project
import re
import os
import csv
import sys
import mparse_util
import logging
import pandas as pd

path1 = "/home/dcfehder/Dropbox/projects/mom_parser/"
file1 = "3021 diet recall 3 25 10.txt"
aa = mparse_util.var_extract(path1, file1)

# this gets the ones that columnsI care about
c= '/home/dcfehder/Dropbox/projects/mom_parser/mparse.sqlite'
ind = mparse_util.load_masterNutrient(c)
trans = mparse_util.load_matchTable(c)

data_dict = mparse_util.translate(aa, c)
data_dict["date"] = mparse_util.sample_date(path1 + file1)

# this puts them into a series object
gg = pd.Series(data_dict, index = ind)

# next, you just want to add a column with that series in a DataFrame



## ## Set path to allow importation of the mom parser class
## if "C:\\emacs\\mom_parser\\" not in sys.path:
##     sys.path.append("C:\\emacs\\mom_parser")

## ## initializations . . . eventually we want to loope over all the open files 
## file_in_path = "C:\\emacs\\mom_parser\\"

## #set the logger path and load logger
## log_path = "C:\\emacs\\mom_parser\\script.log"
## logging.basicConfig(filename= log_path,level=logging.DEBUG)


## #This is the function to check the existice of an entrie in the remapping table in the a_nutrient_observation
## def find_key(dic, val):
##     """return the key of dictionary dic given the value"""
##     try:
##         return [k for k, v in dic.iteritems() if v == val]
    
##     except IndexError:
##         pass

## def key_match(key, string):
##     """checks the two possible combinations of the placement of the key in the multicolumn table"""
##     keypass1 = 
##     try:
        


## def key_checker(file_in_path, files):
    
##     file_path = file_in_path + files
##     fl = open(file_path, 'r+')
##     read = fl.read()
##     counter = 0
##     counter_bad = 0
    
##     f = mom_parser.a_nutrient_observation()
##     goodKeyList = f.data_list
##     mappingKeys = f.remapDic

##     try:
##         for key in goodKeyList:
##             #this checks to see if the key exists
##             if re.search(re.escape(key),read):
##                 #do something here?
##                 counter = counter + 1
##             else:
##                 a = []
##                 a = find_key(mappingKeys, key)
##                 if len(a)>0:
##                     for key_sub in a:
##                         if re.search(re.escape(key_sub),read):
##                             read2 = re.sub(re.escape(key_sub), re.escape(key),read)
##                             read2 = read2.replace("\\","")
##                         else:
##                             counter_bad = counter_bad + 1
##                     #Now you should have made at least one replacement, so you check
##                     if (len(a)-counter_bad)==1:
##                         print "Counter_bad " + str(counter_bad)
##                     else:
##                         logging.debug("PROBLEM with file = %s and key = %s"%(file_path, key))
##                 else:
##                     logging.debug("OVERALL MAPPING PROBLEM with file = %s and key = %s"%(file_path, key))
##     except:
##         print "Loop Error"
##     #now put back the text of the file, because we are done with the searches
##     try:
##         fl.close()
##         fl = open(file_path, 'w')
##         fl.write(read2)
##         fl.close()
##     except:
##         print "file writer error"
##     #We are now trying to check to see if there is a ref to the file in the logger file
##     try:
##         logs = open(log_path, "r")
##         logString = logs.read()
##     except:
##         print "log read error"
    
##     if re.search(file_path,logString):
##         print "Problem with file %s"%s(file_path)
##     else:
##         try:
##             f.parse_data(file_in_path, files)
##             f.csv_writer(file_in_path)
##             print "Successfully Executed"
##         except:
##             print "parser error"
        
                     
## #now get all the files for the loop
## file_list = os.listdir(file_in_path)


## ## Check to make sure that the file is 
## for files in file_list:
##     if files[-3:] == 'txt':
##         #change this now to the newly defined function
##         key_checker(file_in_path, files)
     
##     else:
##         pass


## ## Stuff left over

