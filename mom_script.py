## Author: D Fehder
## Create Date: 6/23/2011
## Purpose: See mom.org file for details on this project
import re, os, csv, sys, mom_parser

## Set path to allow importation of the mom parser class
if "C:\\Users\\dfehder\\Documents\\dev\\mom" not in sys.path:
    sys.path.append("C:\\Users\\dfehder\\Documents\\dev\\mom")


## initializations . . . eventually we want to loope over all the open files 
file_in_path = "C:\\Users\\dfehder\\Documents\\dev\\mom"
file_list = os.listdir(file_in_path)


## Check to make sure that the file is 
for files in file_list:
    if files[-3:] == 'txt':

        f = mom_parser.nutrient_observation()
        f.parse_data(file_in_path, files)
        f.csv_writer(file_in_path)

    else:
        pass


## Stuff left over

