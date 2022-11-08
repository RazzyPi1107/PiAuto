import subprocess
import csv
import os

file = '/home/kali/PiAuto/t.txt'

with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:

        try :
            strg = str ("sudo pip3 install ") + str(row[0])
            print (strg)
            os.system(strg)

        except Exception as e: print(e)
