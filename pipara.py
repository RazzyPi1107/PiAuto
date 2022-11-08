import os
import time
from csv import writer
import datetime
import telepot
from telepot.loop import MessageLoop


#Calculate CPU temperature of Raspberry Pi in Degrees C
temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
print (temp)

if temp > 70:

    msgg = str('🔥🔥🔥🔥 PI 🔥🔥🔥🔥 ') + str (temp)

    try:
        bot.sendMessage(chat_id, str(msgg))

    except:
        print(" ")
