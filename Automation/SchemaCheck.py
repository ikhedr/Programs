#Complexity: O(n^2) -> O(n*f) ..where 'n' is number of rows in csv file & 'f' is number of files in the directory
#Scenario:   
# We have text files at location “C:/CurrentWeek/”. 
# Each file contains columns separated by  “|~”.
# First row of each file is column names and rest of rows contains data of a table(text file is named after table name). 
# These text files columns names (schema) are updated one. 
# On the other side we have “C:/OldSchema.csv” file, containing column names corresponding to respective tables.
#This programs checks whether old column names in OldSchema.csv file matching the current column names in text files.
 #Hey staging

import sys
import os
col_csv = 0
col_txt = 0
tmp = ''
mismatch = 0
isThereFileflg = 0
def SchemaCheck():
    log = open("C:\\Programming\\Python\\log.txt","w+")
    for i in range(rows): #Rows in csv file. In my case rows were 50000
        global col_csv, isThereFileflg, col_txt, col_csv, tmp, mismatch
        A, B = csv.readline().strip().split(',')
        if(A!=''):
            if(col_txt == col_csv and isThereFileflg == 1 and mismatch == 0):
                log.write("Success: for file : %s\n"%tmp) #Specified table columns in OldSchema.txt are matching with current txt file columns
            elif(isThereFileflg == 1 and mismatch == 1):
                log.write("Failure: There is column mismatch in file:%s\n"%tmp)
            elif(isThereFileflg == 1):
            	log.write("Failure: Extra columns in file:%s"%tmp)

            col_csv = 0
            A = str.replace(A,"_YYYYMMDD.txt","_20180215.txt_A") # column A in csv contains TableName_YYYYMMDD.txt name, we gonna replace it with latest file(Today- 21 feb 2018) from C:/CurrentWeek/ repository file with _A type
            isThereFileflg = 0
            for aFile in os.listdir("C:\\Programming\\Python\\"):
            	if(aFile.upper().find(A.upper(),0,len(aFile)) >= 0):
                    columnList = open("C:\\Programming\\Python\\"+aFile,'r').readline().strip("\n").split("|~")
                    col_txt = len(columnList)
                    isThereFileflg = 1
                    tmp = aFile
            	#whether filename in csv match text filename in directory open the text file and collect all columns into list
            if(not isThereFileflg):
                log.write("Failure: There is no production txt file:%s in C:/currentWeek\n"%A)
                isThereFileflg = 2 #flag 2 for txt file not exist in CurrentWeek directory
                continue
        try:
            if(B.upper().find(columnList[col_csv].upper())>=0):
                col_csv += 1
                continue
            elif(isThereFileflg == 1):
                log.write("Failure: For Column name:%s\n"%B)
                mismatch = 1
        except:
            log.write("Failure: Less columns in text file.\n")

    #for last row in csv
    if(col_txt == col_csv and isThereFileflg == 1):
        log.write("Success: For the file: %s\n"%tmp) #Specified table columns in OldSchema.txt are matching with current txt file columns
    elif(isThereFileflg != 2):
        log.write("Failure: Extra columns in txt file:%s\n"%tmp)

rows = 10
csv = open("C:\\Programming\\Python\\OldSchema.csv",'r')
print("\n\n_______________________________________________________________\n")
SchemaCheck()
csv.close()