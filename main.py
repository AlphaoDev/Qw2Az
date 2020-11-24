# -*- coding: utf-8 -*-

from pathlib import Path
import os

qwerty = ["!","@","#","$","%","^","&","*","(",")","-","_","Q","W","A","Z","{","[","}","]",":",";",'"',"'","|","\\","M","m","<",",",">",".","?","/"]
azerty = ["1","2","3","4","5","6","7","8","9","0",")","°","A","Z","Q","W","¨","^","£","$","M","m","%","ù","µ","*","?",",",".",";","/",":","§","!"]

def toQwStr(string):
    data = ''
    for c in string:
        if c in qwerty:
            for i in range (len(qwerty)):
                if qwerty[i] == c:
                    data += azerty[i]
        else:
            data +=c
    print("")
    print("The final string is : ",data)

def toQwFile(file):
    pathfile = Path("{}\{}".format(os.getcwd(),file))
    filename = file.replace(".txt","")
    if pathfile.is_file():
        data = ''
        with open(file,"r") as rd_file:
            for line in rd_file:
                for c in line:
                    if c in qwerty:
                        for i in range (len(qwerty)):
                            if qwerty[i] == c:
                                data += azerty[i]
                    else:
                        data +=c
                with open("{}_ToAzerty.txt".format(filename),"w") as wr_file:
                    wr_file.write(data)
                    
        print(pathfile)
        print("ok")
    else:
        print("The file doesn't exist in {} directory.".format(os.getcwd()))

def getTable():
    data = [qwerty, azerty]
    col_width = max(len(word) for row in data for word in row) + 2
    for row in data:
        print ("".join(word.ljust(col_width) for word in row))

print("")
print("1 - Conversion table")
print("2 - Convert a file")
print("3 - Convert a string")
print("")

choice = int(input("Choose an action (1/2/3): "))

if choice == 3:
    string = str(input("Type string: "))
    toQwStr(string)
elif choice == 2:
    print("Make sur that your file is in {} directory.".format(os.getcwd()))
    file = str(input("Type filename: "))
    toQwFile(file)
elif choice == 1:
    print("Here is the conversion table : ")
    getTable()
else:
    print("Please select a number between 1 and 3.")
