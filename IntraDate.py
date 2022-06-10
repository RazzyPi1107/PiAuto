#######################################

import yfinance as yf
import pandas as pd
import time
import schedule
import datetime
from datetime import date, timedelta
import numpy as np
from pandas import ExcelWriter
import csv
import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import os
import telepot
from telepot.loop import MessageLoop
from time import strftime
import telepot
from telepot.loop import MessageLoop
import time


SymbolNS ='^NSEBANK'

aa = yf.Ticker(SymbolNS) #Ticker name from yahoo.com

aa = aa.history('3y')
print (aa)
j1 = aa.shape[0]

Tday =[]
Yday=[]
TommD = []
Tomm = datetime.date.today() + datetime.timedelta(days=1)
print (Tomm)
print (j1)
j2 = j1 -1
j3 = j1 -2
a2 = aa.index[j2]


y3=int (a2.strftime("%Y"))
m3=int (a2.strftime("%m"))
d3=int (a2.strftime("%d"))
h3=int (a2.strftime("%H"))

print (y3,m3,d3)
today = str(y3)+str('-')+str(m3)+str('-')+str(d3)
a3 = aa.index[j3]


y13=int (a3.strftime("%Y"))
m13=int (a3.strftime("%m"))
d13=int (a3.strftime("%d"))
h13=int (a3.strftime("%H"))

yesterday = str(y13)+str('-')+str(m13)+str('-')+str(d13)
Tomm = datetime.date.today() + datetime.timedelta(days=1)

print (y13,m13,d13)

Tday.append(today)
Yday.append(yesterday)
TommD.append(Tomm)

datab ={'Tday':Tday, 'Yday':Yday, 'Tomm':TommD}
dff = pd.DataFrame(datab)

print (dff)

filnamor = str('Dates')+str('.csv')
dff.to_csv(filnamor)
