import time,datetime
import os, shutil
import telepot
import time
import schedule
import datetime

tod = datetime.datetime.now()

HHR = tod.hour
MMN = tod.minute

#Monday is 0 and Sunday is 6
dday = datetime.datetime.today().weekday()

if HHR == 9 and MMN == 17:
    os.system('sudo python3 /home/kali/PiAuto/Loop.py')