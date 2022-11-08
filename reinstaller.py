import subprocess
import csv
import os

file = '/home/kali/PiAuto/ins.txt'

with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:

        try :
            strg = str(row[0])
            print (strg)
            os.system(strg)

        except Exception as e: print(e)
