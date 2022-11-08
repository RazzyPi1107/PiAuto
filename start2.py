import os
import time
from csv import writer
import datetime
import telepot
from telepot.loop import MessageLoop

LISTT=['1047135684'  , '@CamCamCam',  '1001739086451', '@1001739086451', 'CamCam', '@731859043', '731859043']


bot = telepot.Bot('1447565647:AAG9OPZq1xE68hj0uQvk0k6QKgticqaTO_I')

for i in LISTT:

    chat_id = str(i)

    tod = datetime.datetime.now()
    print (i, '  |  ', tod)

    msgg = str('Pi ON : ')  +  str (tod)


    try:
        bot.sendMessage(chat_id, str(msgg))
    except:
        print("End")

