import os
import time
from csv import writer
import datetime
import telepot
from telepot.loop import MessageLoop
import os
import time
from csv import writer
import datetime
import telepot
from telepot.loop import MessageLoop
import os



def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

tttts = get_ip_address()

a2 = datetime.datetime.now()
print (tod)
a2 = datetime.datetime.now()
y3=int (a2.strftime("%Y"))
m3=str (a2.strftime("%b"))
d3=int (a2.strftime("%d"))
h3=int (a2.strftime("%H"))
M3=int (a2.strftime("%M"))
today = str(d3)+str('-')+str(m3)+str('-')+str(y3) +str(' | ') + str(h3)+str(':')+str(M3)
print (today)
try:
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
except:
    temp = 100
print (temp)


msgk = str('Pi ON : ')  +  str (today) + str(' ') + str('\n' + str (temp)  + str('\n') + str (tttts)

bot = telepot.Bot('5226423541:AAHQ4s7Pl-COf6-5-nBOMk7oJM3dax1SW8U')
chat_id = '1047135684'
bot.sendMessage(chat_id, str(msgk))

