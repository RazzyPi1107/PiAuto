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
import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np
import IntraDate



bot = telepot.Bot('1356204823:AAHY1lxuINcDabR6mfrRYMP-ojd11IcYna8')
chat_id = '1047135684'

df = pd.read_csv('/home/kali/PiAuto/Intraday.csv')

SymbolNS =df["Symbol"]


bbot = telepot.Bot('5226423541:AAHQ4s7Pl-COf6-5-nBOMk7oJM3dax1SW8U')
chat_id = '1047135684'

file = 'Dates.csv'
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV :

        today = row[1]
        yesterday = row[2]
        Tomm = row[3]

MSGK = " "
COUNTR0 = 0

for i in SymbolNS:
    stk = i
    print (i)
    REDY = '#ff0000'
    GREENY = '#00ff00'
    NORMALL = '#120052'
    COL1 = '#120052'
    COL2 = '#120052'
    COL3 = '#120052'
    COL4 = '#120052'
    COL5 = '#120052'
    COL6 = '#120052'
    a2 = datetime.datetime.now()
    y3 = int(a2.strftime("%Y"))
    m3 = int(a2.strftime("%m"))
    d3 = int(a2.strftime("%d"))
    h3 = int(a2.strftime("%H"))
    M3 = int(a2.strftime("%M"))
    TYME = str(h3) + str(" : ") + str(M3)


    print(y3, m3, d3)
    today = str(y3) + str('-') + str(m3) + str('-') + str(d3)


    aa = yf.download(i, start=today , end=Tomm, interval = "1m",progress=False)
    print (aa)


    aa['30MAM'] = aa.Close.rolling(20).mean() #Bollineger Band mean
    aa['30MASD'] = aa.Close.rolling(20).std() #Bollineger Band std dev

    aa['Bub'] = aa['30MAM'] + (aa['30MASD'] *2) #Bollineger  Upper Band
    aa['Blb'] = aa['30MAM'] - (aa['30MASD'] *2) #Bollineger Lower Band

    aa['ShortEMA'] =aa.Close.ewm(span=12, adjust=False).mean()
    # long term EMA
    aa['LongEMA'] = aa.Close.ewm(span=26, adjust=False).mean()
    # MACD line
    aa['MACD'] = aa['ShortEMA'] - aa['LongEMA']
    # MACD Singal line

    aa['signal'] = aa['MACD'].ewm(span=9, adjust=False).mean()
    nkm = aa['signal'].shape[0]
    aa['Nan']= np.nan
    aa ['Calling']=aa['MACD']-aa['signal']
    # 50 EMA : Beep Boop Strategy
    aa['EMA50'] = aa.Close.ewm(span=50, adjust=False).mean()
    aa['EMA200'] = aa.Close.ewm(span=200, adjust=False).mean()

    def computeRSI (data, time_window):

        #R
        diff = data.diff(1).dropna()        # diff in one field(one day)

        #this preservers dimensions off diff values
        up_chg = 0 * diff
        down_chg = 0 * diff

        # up change is equal to the positive difference, otherwise equal to zero
        up_chg[diff > 0] = diff[ diff>0 ]

        # down change is equal to negative deifference, otherwise equal to zero
        down_chg[diff < 0] = diff[ diff < 0 ]

        # check pandas documentation for ewm
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
        # values are related to exponential decay
        # we set com=time_window-1 so we get decay alpha=1/time_window
        up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
        down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()

        rs = abs(up_chg_avg/down_chg_avg)
        rsi = 100 - 100/(1+rs)
        return rsi


    aa['RSI'] = computeRSI(aa['Close'], 14)

    aa['dife']=aa['Close'].diff()

    aa['50MA'] = aa.Close.rolling(50).mean()  # 50 day moving avg
    aa['200MA'] = aa.Close.rolling(200).mean()  # 200 day moving avg
    aa['52WH'] = aa.High.rolling(256).max()  # 256 is number of rows
    aa['52WL'] = aa.Low.rolling(256).min()  # 256 is number of rows
    aa['%ofL'] = round(aa['Close'] / aa['52WL'], 2)  # 52Week Low from that day
    aa['%ofH'] = round(aa['Close'] / aa['52WH'], 2)  # 52Week High from that day
    aa['30MAM'] = aa.Close.rolling(20).mean()  # Bollineger Band mean
    aa['30MASD'] = aa.Close.rolling(20).std()  # Bollineger Band std dev
    aa['50MAH'] = aa.Close.rolling(50).max()  # 50 is number of rows
    aa['50MAL'] = aa.Close.rolling(50).min()  # 50 is number of rows

    aa['Bub'] = aa['30MAM'] + (aa['30MASD'] * 2)  # Bollineger  Upper Band
    aa['Blb'] = aa['30MAM'] - (aa['30MASD'] * 2)  # Bollineger Lower Band
    aa['BBlwratio'] = aa['30MAM'] - aa['Blb']
    aa['BBPrratio'] = aa['Close'] - aa['Blb']
    aa['BBratio'] = aa['BBPrratio'] / aa['BBlwratio']

    aa['Volumem'] = aa.Volume.rolling(3).mean()  # 50 day moving avg
    aa['Volumesd'] = aa.Volume.rolling(2).std()  # 50 day moving avg
    aa['Volumesdm'] = aa.Volumesd.rolling(3).mean()  # 50 day moving avg
    aa['Doji'] = aa['Close'] - aa['Open']  # Cal Doji location
    # short term EMA
    aa['ShortEMA'] = aa.Close.ewm(span=12, adjust=False).mean()
    # long term EMA
    aa['LongEMA'] = aa.Close.ewm(span=26, adjust=False).mean()
    # MACD line
    aa['MACD'] = aa['ShortEMA'] - aa['LongEMA']
    # MACD Singal line

    aa['signal'] = aa['MACD'].ewm(span=9, adjust=False).mean()
    nkm = aa['signal'].shape[0]
    aa['Nan'] = np.nan
    aa['Calling'] = aa['MACD'] - aa['signal']
    # 50 EMA : Beep Boop Strategy
    aa['EMA50'] = aa.Close.ewm(span=50, adjust=False).mean()
    aa['1D'] = aa.Close.diff()
    aa['v1d'] = aa['1D'] * aa['Volume']
    aa['v1dd'] = aa.v1d.diff()

    aa['Time'] = aa.index


    aa['BBLR'] = aa['Blb']/aa['Low']
    aa['BBUR'] = aa['Bub']/aa['High']


    dl = len (aa)

    aa['DIR'] = 0
    aa['DIRP'] = 0
    aa['MACDir'] = 0
    aa['MACDRati'] = 0

    for i in range (0, dl):
        if (aa["Open"][i]) >= (aa["Close"][i]):

            aa['DIR'][i] = -1
            #aa['DIRP'][i] = (aa["Open"][i]) / (aa["Close"][i])

        if (aa["Open"][i]) < (aa["Close"][i]):

            aa['DIR'][i] = 1
            #aa['DIRP'][i] = (aa["Close"][i]) / (aa["Open"][i])

        if aa['MACD'][i] !=0 and  aa['signal'][i] != 0:


            if aa['MACD'][i] > aa['Low'][i]:
                aa['MACDir'][i] = 1
                #aa['MACDRati'][i] = aa['MACD'][i] / aa['signal'][i]

            if aa['MACD'][i] <= aa['signal'][i]:
                aa['MACDir'][i] = -1
                #aa['MACDRati'][i] = (aa['signal'][i] / aa['MACD'][i])




    m = len(aa) - 1

    MSGK1 =  str('\n')+ str(int(aa['Close'][m])) + str('\n')+ str(" RSI:")  + str(int(aa['RSI'][m]))+ str('\n') + str(" ") + str(" BLB:")  + str((aa['BBLR'][m])) + str('\n') + str(" ") + str(" BUB:")  + str((aa['BBUR'][m])) + str('\n') + str(" ") + str(" DIFF:")  + str((aa['1D'][m]))  + str('\n') + str(" ") + str(TYME) + str('\n') + str('------------------')+str('\n')



    if ((aa['Blb'][m] / aa['Low'][m])> 1.0002 or aa['RSI'][m] <= 25) and aa['1D'][m]<0:
        print ("1")
        COUNTR0 = 100000
        COL1 = REDY
        Target = (int(aa['Close'][m]) ) + 25
        MSGK = MSGK + str(" ") + str(stk) + str("🟢🟢🟢 BUY 🟢🟢🟢") + MSGK1

    elif ((aa['Bub'][m] / aa['High'][m])>1.0002 and aa['RSI'][m] >= 75) and aa['1D'][m]>0:

        COUNTR0 = 100000
        COL1 = GREENY
        Target = (int(aa['Close'][m])) - 25
        MSGK = MSGK + str(" ") + str(stk) + str("🔴 🔴 🔴 SELL 🔴 🔴 🔴") + MSGK1

    m = len(aa) - 2

    if ((aa['Blb'][m] / aa['Low'][m])>1.0002 or aa['RSI'][m] <= 25) and aa['1D'][m]<0:
        COUNTR0 = 100000
        COL1 = REDY
        Target = (int(aa['Close'][m])) + 25
        MSGK = MSGK + str(" ") + str(stk) + str(" 🟢🟢🟢 BUY 🟢🟢🟢") + MSGK1

    elif ((aa['Bub'][m] / aa['High'][m])>1.0002 and aa['RSI'][m] >= 75) and aa['1D'][m]>0:

        COUNTR0 = 100000
        COL1 = GREENY
        Target = (int(aa['Close'][m])) - 25
        MSGK = MSGK + str(" ") + str(stk) + str("🔴 🔴 🔴 SELL 🔴 🔴 🔴") + MSGK1

    print (MSGK)

    if COUNTR0 > 0:
        bbot.sendMessage(chat_id, str(MSGK))

print ("Done1")
















