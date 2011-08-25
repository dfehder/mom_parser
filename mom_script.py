## Author: D Fehder
## Create Date: 6/23/2011
## Purpose: See mom.org file for details on this project
import re, os, csv, sys, mom_parser

## Set path to allow importation of the mom parser class
if "C:\\emacs\\mom_parser\\" not in sys.path:
    sys.path.append("C:\\emacs\\mom_parser")

#This is the function to check the existice of an entrie in the remapping table in the a_nutrient_observation
def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    try:
        return [k for k, v in dic.iteritems() if v == val]
    
    except IndexError:
        pass

#I am going to take from below and put it into the key_checker
o = <strong class="highlight">open</strong>("output","a") #open for append
for line in <strong class="highlight">open</strong>("<strong class="highlight">file</strong>"):
       line = line.replace("someword","newword")
   o.write(line + "\n") 
o.close()

def key_checker(goodKeyList, mappingKeys,  file):
    fl = open(file, 'r+')
    read = fl.read()

    for key in goodKeyList:
        #this checks to see if the key exists
        if re.search(re.escape(key),read):
            
        
    


## initializations . . . eventually we want to loope over all the open files 
file_in_path = "C:\\emacs\\mom_parser"
file_list = os.listdir(file_in_path)


## Check to make sure that the file is 
for files in file_list:
    if files[-3:] == 'txt':

        f = mom_parser.a_nutrient_observation()
        f.parse_data(file_in_path, files)
        f.csv_writer(file_in_path)

    else:
        pass


## Stuff left over

