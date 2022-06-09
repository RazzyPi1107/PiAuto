import time,datetime
import os, shutil
import telepot
import time
import schedule
import datetime
from gpiozero import CPUTemperature

tod = datetime.datetime.now()

HHR = tod.hour
MMN = tod.minute
bot = telepot.Bot('1356204823:AAHY1lxuINcDabR6mfrRYMP-ojd11IcYna8')
chat_id = '1047135684'

cpu = CPUTemperature()
print(cpu.temperature)

#Monday is 0 and Sunday is 6
dday = datetime.datetime.today().weekday()

if HHR == 9 and MMN == 17:
    os.system('sudo python3 /home/kali/PiAuto/Loop.py')

if HHR > 7 and HHR <= 23 and MMN == 5:
    bot.sendMessage(chat_id, str(cpu.temperature))