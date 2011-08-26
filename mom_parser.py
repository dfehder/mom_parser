## Author: D Fehder
## Create Date: 6/23/2011
## Purpose: See mom.org file for details on this project
import re, os, csv

## This begins the class object nutrient_observation. The point of this class is to collect the parsing steps and the export steps associated with the
## Retrieval into one place

class a_nutrient_observation:
    def __init__(self):

        self.subjectid = ""
        self.dated = ""
        
        self.data_list = ['Gram Weight (g)','Biotin (mcg)','Vitamin C (mg)','Calories (kcal)','Vitamin D - IU (IU)','Calories from Fat (kcal)',
                          'Vitamin D - mcg (mcg)','Calories from SatFat (kcal)','Vitamin E - Alpha-Toco (mg)','Protein (g)','Folate (mcg)',
                          'Carbohydrates (g)','Folate, DFE (mcg)','Dietary Fiber (g)','Vitamin K (mcg)','Soluble Fiber (g)','Pantothenic Acid (mg)',
                          'Total Sugars (g)','Monosaccharides (g)','Calcium (mg)','Disaccharides (g)','Chromium (mcg)','Other Carbs (g)','Copper (mg)',
                          'Fat (g)','Fluoride (mg)','Saturated Fat (g)','Iodine (mcg)','Mono Fat (g)','Iron (mg)','Poly Fat (g)','Magnesium (mg)',
                          'Trans Fatty Acid (g)','Manganese (mg)','Cholesterol (mg)','Molybdenum (mcg)','Water (g)','Phosphorus (mg)','Potassium (mg)',
                          'Vitamin A - IU (IU)','Selenium (mcg)','Vitamin A - RAE (RAE)','Sodium (mg)','Carotenoid RE (RE)','Zinc (mg)',
                          'Retinol RE (RE)','Beta-Carotene (mcg)','Omega 3 Fatty Acid (g)','Vitamin B1 (mg)','Omega 6 Fatty Acid (g)',
                          'Vitamin B2 (mg)','Vitamin B3 (mg)','Alcohol (g)','Vitamin B3 - Niacin Equiv (mg)','Caffeine (mg)','Vitamin B6 (mg)',
                          'Choline (mg)','Vitamin B12 (mcg)']

        self.nutrient_data = {'Gram Weight (g)':'','Biotin (mcg)':'','Vitamin C (mg)':'','Calories (kcal)':'','Vitamin D - IU (IU)':'',
                              'Calories from Fat (kcal)':'','Vitamin D - mcg (mcg)':'','Calories from SatFat (kcal)':'','Vitamin E - Alpha-Toco (mg)':'',
                              'Protein (g)':'','Folate (mcg)':'','Carbohydrates (g)':'','Folate, DFE (mcg)':'','Dietary Fiber (g)':'','Vitamin K (mcg)':'',
                              'Soluble Fiber (g)':'','Pantothenic Acid (mg)':'','Total Sugars (g)':'','Monosaccharides (g)':'','Calcium (mg)':'',
                              'Disaccharides (g)':'','Chromium (mcg)':'','Other Carbs (g)':'','Copper (mg)':'','Fat (g)':'','Fluoride (mg)':'',
                              'Saturated Fat (g)':'','Iodine (mcg)':'','Mono Fat (g)':'','Iron (mg)':'','Poly Fat (g)':'','Magnesium (mg)':'',
                              'Trans Fatty Acid (g)':'','Manganese (mg)':'','Cholesterol (mg)':'','Molybdenum (mcg)':'','Water (g)':'',
                              'Phosphorus (mg)':'','Potassium (mg)':'','Vitamin A - IU (IU)':'','Selenium (mcg)':'','Vitamin A - RAE (RAE)':'',
                              'Sodium (mg)':'','Carotenoid RE (RE)':'','Zinc (mg)':'','Retinol RE (RE)':'','Beta-Carotene (mcg)':'',
                              'Omega 3 Fatty Acid (g)':'','Vitamin B1 (mg)':'','Omega 6 Fatty Acid (g)':'','Vitamin B2 (mg)':'','Vitamin B3 (mg)':'',
                              'Alcohol (g)':'','Vitamin B3 - Niacin Equiv (mg)':'','Caffeine (mg)':'','Vitamin B6 (mg)':'','Choline (mg)':'',
                              'Vitamin B12 (mcg)':''}

        self.remapDic = {"Vitamin B1 - Thiamin (mg)":"Vitamin B1 (mg)"}

    def parse_data(self, file_into_path, file_into_name):
      
        ## Take the file in path and open the file
        file_namers = file_into_path + "\\" + file_into_name
        file_in = open(file_namers, 'r')
        
        ## Not get the subject number
        ##file_proc = file_into_path.split('\\')
        ##file_name = file_proc.pop()
        
        self.subjectid = file_into_name[:4]

         ## get the date information with a regular expression
        file_name_noext = file_into_name[:-4]

        pattern1  = "[0-9]{1,2} [0-9]{1,2} [0-9][0-9]$"

        if re.search(pattern1, file_name_noext):
            date_samp = re.search(pattern1, file_name_noext).group().replace(" ", "/")
            self.dated = date_samp

        else:
            pass
        
        
        ## rope throught the file and assign the values to the right keys of the nutrient_data dictionary
        double_tab = '\t\t'
        triple_tab = '\t\t\t'
        tab_space_tab = '\t \t'

        for line in file_in:
            if re.search(double_tab, line):
                b = line.split(double_tab)
                b1 = b[0].split('\t')
                b2 = b[1].split('\t')
                
                if self.nutrient_data.has_key(b1[0]):
                    try:
                        self.nutrient_data[b1[0]] = b1[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line
                    
                else:
                    pass
                
                if self.nutrient_data.has_key(b2[0]):
                    try:
                        self.nutrient_data[b2[0]] = b2[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line
                else:
                    pass
                
            else:
                pass
            
            if re.search(triple_tab, line):
                b = line.split(triple_tab)
                b1 = b[0].split('\t')
                b2 = b[1].split('\t')

                if self.nutrient_data.has_key(b1[0]):
                    try:
                        self.nutrient_data[b1[0]] = b1[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line

                else:
                    pass

                if self.nutrient_data.has_key(b2[0]):
                    try:
                        self.nutrient_data[b2[0]] = b2[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line
                else:
                    pass
                
            else:
                pass
            
            if re.search(tab_space_tab, line):
                a = line.lstrip(' \t')
                a = a.rstrip('\t ')
                b = a.split(tab_space_tab)
                b1 = b[0].split('\t')
                b2 = b[1].split('\t')
                
                if self.nutrient_data.has_key(b1[0]):
                    try:
                        self.nutrient_data[b1[0]] = b1[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line
                else:
                    pass

                if self.nutrient_data.has_key(b2[0]):
                    try:
                        self.nutrient_data[b2[0]] = b2[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line

                else:
                    pass

            else:
                pass


            if re.search("^Vitamin B12", line):
                b = line.split('\t')
                
                if self.nutrient_data.has_key(b[0]):
                    try:
                        self.nutrient_data[b[0]] = b[1].rstrip('\n')
                    except IndexError:
                        print "Sub:" + self.subjectid + "Date" + self.dated + "Line:" + line
                else:
                    pass
            else:
                pass
    
    
    def csv_writer(self, pwd):
        ## This is the stuff to get it into the central csv file
        ## Check to see if there is a central csv in the pwd
        
        csv_out_path = pwd + '\\mom_parse_output.csv'
        
        if os.path.exists(csv_out_path):
            pass
        
        else:
            ## write the header
            mod_list = ['Subject ID', 'Sample Date'] + self.data_list
            csv_file = open(csv_out_path,'wb')
            csv_writer1 = csv.writer(csv_file, dialect='excel')
            csv_writer1.writerow(mod_list)
            csv_file.close()
            
        
        ## Generate the list for the line for each individual
        nutrient_data_list = []
        for elem in self.data_list:
            nutrient_data_list.append(self.nutrient_data[elem])

        ## now write the line
        row_add = [self.subjectid, self.dated] + nutrient_data_list
        csv_file = open(csv_out_path,'ab')
        csv_writer1 = csv.writer(csv_file, dialect='excel')
        csv_writer1.writerow(row_add)
        csv_file.close()

