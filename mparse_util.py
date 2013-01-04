# The purpose of this file is to contain different functions required to do mom's parsing
import os, pickle, re, datetime, sqlite3, logging, pandas
import numpy as np

#path1 = "/home/dcfehder/Dropbox/projects/mom_parser/"
#file1 = "3021 diet recall 3 25 10.txt"
#aa = mparse_util.var_extract(path1, file1)


#/////////////////////////////////////////
#\\\    Error Logging Configuration   \\\\
#/////////////////////////////////////////
 

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('mparse')
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.INFO)

# create file handler which logs even debug messages
fh = logging.FileHandler('/home/dcfehder/Dropbox/projects/mom_parser/mparse.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)




#/////////////////////////////////////////
#\\\          Sub- Functions         \\\\
#/////////////////////////////////////////

def return_finder(file_str, strt_pos):
    """
    Finds the next line containing only a hard return
    after the start position strt_pos
    """
    pattern = re.compile("\n\r\n")
    ab = pattern.search(file_str, strt_pos)
    end = ab.start()
    logger.debug(type(end))
    return end 


def sub_id(file_str):
    #find the subject id
    a = file_str.find("Person:")
    if a > -1:
        
        #The regular expression below attempts to extract the id number
        m = re.match(r"Person:(?P<id_num>.*?)\r",file_str)
        num = m.group('id_num').strip()
        logger.debug("got to end of sub_id func")
        return num

    else:
        logger.error("NO PERSON DELIMITER, SO FAIL IN SUB_ID FUNC")


def sample_date(file_name):
    """
    This identifies the date of the sample.
    Right now, it looks for a very specific regular expression.
    It might be worth thinking about more general forms
    """
    a = file_name.find("diet recall")
    logger.debug("FUNC sample_data:: debug 1, file named=  %s"%(file_name))
    startSlice = a + 11
    if a > -1:

         slicer = file_name[startSlice:]
         #This knocks out white space and then returns day month year
         m = re.match(r".*?(?P<mm>\d+) (?P<dd>\d+) (?P<yyyy>\d+).txt", slicer)
         dater = "%s/%s/%s" % (m.group('mm'), m.group('dd'), m.group('yyyy'))
         return dater
     
    else:
        logger.error("FUNC sample_data:: error 1, file name = %s"%(file_name))

def data_extract(file_str):
    """
    This function finds the data portion:
    It looks for 'Multi Column' and then extracts
    until the first hard return
    """
    a = file_str.find("Multi Column")
    logger.debug("FUNC data_extract:: start point = %s"%(str(a)))
    if a>-1:
        #f_sub1 = file_str[a:]
        # now find the end point of the data
        end_point = return_finder(file_str, a)
        logger.debug("FUNC data_extract: end_point = %s"%(str(end_point)))
        logger.debug(type(end_point))
        if end_point > -1:
            # if there is an endpoint, then return that subsection
            f_sub2 = file_str[a:end_point]
            return f_sub2
        else:
            logger.error("FUNC data_extract: No endpoint")
    else:
        logger.error("FUNC data_extract: No Multi Column in text")


def load_matchTable(sql_path):
    """
    This function loads the sqlite file with a table called
    This table ???????
    """
    exec1 = "select * from match_table"
    conn = sqlite3.connect(sql_path)
    res = conn.execute(exec1)
    return dict(res)

def load_masterNutrient(sql_path):
    """
    This function loads the elements of the master nutrient table
    into a list which allows me to create the columns of the pandas
    sheet object
    """
    exec1 = "select * from match_table"
    conn = sqlite3.connect(sql_path)
    res = conn.execute(exec1)

    return list(res)
    
    
    

    

## x = np.zeros((1,),dtype=('i4,f4,a10'))


#/////////////////////////////////////////
#\\\          Main Functions          \\\\
#/////////////////////////////////////////


def var_extract(path, file):
    """
    This function returns a dictionary with
    the various variable/value pairs in the set
    """
    #first define a local dict and load the file
    ret_dict = {}
    f = open(path + file, "r")
    f_str = f.read()

    #now get the data part
    file_str = data_extract(f_str)
    
    #Overall there will be three loops mapping
    #to the three potential cases of value (decimal, zero, double dash)
    
    # reexp for decimal
    decimal = r".*?(?P<nomme>[[a-zA-Z][^\t\n\r]+)\t(?P<value>\d+\.\d+)"
    zero = r".*?(?P<nomme>[[a-zA-Z][^\t\n\r]+)\t(?P<value>0)"
    doubledash = r".*?(?P<nomme>[[a-zA-Z][^\t\n\r]+)\t(?P<value>--)"
    
    cases = [decimal, zero, doubledash]
    
    # function that takes the regexp and loops
    def var_dict(st, reg_pat):
        """
        Takes pattern and extracts those variables
        """
        try:
            for elem in re.finditer(reg_pat,st):
                namer = elem.group('nomme')
                ret_dict[namer] = elem.group('value')
                logger.debug("FUNC var_extract:: entered %s"%(str(namer)))
        except:
            logger.error("FUNC var_extract:: %s"%(reg_pat))
            
    logger.debug("FUNC var_extract:: start loop on %s"%(file))    
    for elem in cases:
        var_dict(file_str, elem)

    return ret_dict
 
    
def variable_ctrl(file_str, pickle_file):
    #This function makes sure that each of the variables in the file is in the master sheet
    cc = variable_ext(file_str)
    f = open(pickle_file, 'r')
    unpickler = pickle.Unpickler(f)
    master = unpickler.load()

    checker = []
    for elem in cc.iterkeys():
        if master.has_key(elem):
            pass
        else:
            #add the element to the checker
            checker.append(elem)

    #now check to see if the loop returned any bad keys
    if len(checker) > 0:
        return checker
    else:
        return cc

def csvLine(delim, list):
    #This function takes a list and returns a formatted string to be written to a file given a specific seperator

    ret_str = ""
    if len(list)<1:
        return ret_str + "\n"
    else:
        #add the first element without the delimitor
        ret_str = str(list.pop(0))
        for elem in list:
            ret_str = ret_str + delim + str(elem)

        #now add the final page break
        ret_str = ret_str + "\n"

        return ret_str

    

     



    
    

