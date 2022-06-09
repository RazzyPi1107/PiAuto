import yfinance as yf
import pandas as pd
import time
import schedule
import datetime
from datetime import date, timedelta
import numpy as np
import telepot
from telepot.loop import MessageLoop
from pandas import ExcelWriter
from tabulate import tabulate
import csv
import requests

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import os
import telepot
from telepot.loop import MessageLoop


bot = telepot.Bot('1356204823:AAHY1lxuINcDabR6mfrRYMP-ojd11IcYna8')
chat_id = '1047135684'

tod = datetime.datetime.now()






StkList = []
Price =  []
C1D = []
C3D = []
C7D = []
C10D = []
C15D = []
C30D = []
WH52 = []
WL52 = []
RISK = []
MACDm = []
MACDmB =[]
BBmem =[]
BBmemB = []
BBB=[]
ProfList =[]
ProfPList = []
SellerList =[]

BBratioB = []
EMA50 = []
EMA50B = []
RSI = []
RSIB =[]
MACDf = []
MACDfB = []
WHR = []
WLR = []
EMA50R = []
BBR = []
QTYY = []
TAR2 = []
TAR3 = []
TAR5 = []
TARGET = []
DAYSH = []

SYMBOL = []

total = 0
index = 0
targettt = 0
profits = 0
invests = 0

with open('/home/kali/PiAuto/Portfolio.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')


    for i in readCSV:
        print (i)
        print (i[1])

        #RELIANCE@50@1930@2000@1900@P
        # Reading Text File
        SymbolNS = str(i[0])+str('.NS')
        QTY = float(i[1])
        Bought = float(i[2])
        Target = 1.02*Bought
        symb = str(i[0])



        y1=int (tod.strftime("%Y"))
        m1=int (tod.strftime("%m"))
        d1=int (tod.strftime("%d"))

        todaydate = str(y1)+str("-")+str(m1)+str("-")+str(d1)


        d1 = date(y1, m1, d1)




        fromdate = (i[3])
        dd = fromdate.split('-')
        print (dd[0])
        d0 = date(int(dd[0]), int(dd[1]), int(dd[2]))
        delta = d1 - d0
        print(delta.days)



        aa = yf.Ticker(SymbolNS) #Ticker name from yahoo.com

        aa = aa.history('2y')



        aa.drop(columns=['Dividends','Stock Splits'],inplace=True)
        aa['50MA'] = aa.Close.rolling(50).mean() #50 day moving avg
        aa['200MA'] = aa.Close.rolling(200).mean() #200 day moving avg
        aa['52WH'] = aa.High.rolling(256).max() #256 is number of rows
        aa['52WL'] = aa.Low.rolling(256).min() #256 is number of rows
        aa['%ofL']= round(aa['Close']/aa['52WL'],2) #52Week Low from that day
        aa['%ofH']= round(aa['Close']/aa['52WH'],2) #52Week High from that day
        aa['30MAM'] = aa.Close.rolling(20).mean() #Bollineger Band mean
        aa['30MASD'] = aa.Close.rolling(20).std() #Bollineger Band std dev
        aa['50MAH'] = aa.Close.rolling(50).max() #50 is number of rows
        aa['50MAL'] = aa.Close.rolling(50).min() #50 is number of rows
        aa['BBR'] = aa['Close']/aa['30MAM']
        aa['Bub'] = aa['30MAM'] + (aa['30MASD'] *2) #Bollineger  Upper Band
        aa['Blb'] = aa['30MAM'] - (aa['30MASD'] *2) #Bollineger Lower Band


        aa['WHR'] = (aa['Close']-aa['52WL'])/(aa['52WH']-aa['52WL'])
        aa['WLR'] = 1 - aa['WHR']



        aa['Volumem'] = aa.Volume.rolling(3).mean() #50 day moving avg
        aa['Volumesd'] = aa.Volume.rolling(2).std() #50 day moving avg
        aa['Volumesdm'] = aa.Volumesd.rolling(3).mean() #50 day moving avg
        aa['Doji'] =aa['Close'] - aa['Open'] # Cal Doji location
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
        aa['EMA50R'] = aa['Close']/aa['EMA50']






        def buy_sell (signal):
            Buy=[]
            Sell=[]
            flag = -1

            for m in range (0,len(signal)):
                if aa['MACD'][m]> aa['signal'][m]:
                    Sell.append(np.nan)
                    if flag != 1:
                        Buy.append(aa['Close'][m])
                        flag = 1
                    else:
                        Buy.append(np.nan)
                elif aa['MACD'][m]< aa['signal'][m]:

                    Buy.append(np.nan)
                    if flag != 0:
                        Sell.append(aa['Close'][m])
                        flag = 0
                    else:
                        Sell.append(np.nan)
                else:
                    Buy.append(np.nan)
                    Sell.append(np.nan)

            return (Buy,Sell)

        a = buy_sell(aa)
        aa['SELL'] = a[0]
        aa['BUY'] = a[1]

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


        tod = datetime.datetime.now()
        N = 365 #Chart date range
        d = datetime.timedelta(days = N)
        a = tod - d
        y1=int (tod.strftime("%Y"))
        m1=int (tod.strftime("%m"))
        d1=int (tod.strftime("%d"))
        y2=int (a.strftime("%Y"))
        m2=int (a.strftime("%m"))
        d2=int (a.strftime("%d"))

        fromdate = str(y2)+str("-")+str(m2)+str("-")+str(d2)
        todaydate = str(y1)+str("-")+str(m1)+str("-")+str(d1)

        aa = aa[fromdate : todaydate]# Slicing data to desired date range for visualization


        nn = aa.shape[0]
        nm = nn - 1
        n1 = nm - 1
        n3 = nm - 3
        n7 = nm - 7
        n10 = nm - 10
        n15 = nm - 15
        n30 = nm - 30

        pr=(aa["Close"][nm]).round(1)
        pr1=(aa["Close"][n1]).round(1)
        pr3=(aa["Close"][n3]).round(1)
        pr7=(aa["Close"][n7]).round(1)
        pr10=(aa["Close"][n10]).round(1)
        pr15=(aa["Close"][n15]).round(1)
        pr30=(aa["Close"][n30]).round(1)

        hpr = (aa["High"][nm]).round(1)



        d1 = (((pr-pr1)*100/pr)).round(1)
        d3 = (((pr-pr3)*100/pr)).round(1)
        d7 = (((pr-pr7)*100/pr)).round(1)
        d10 = (((pr-pr10)*100/pr)).round(1)
        d15 = (((pr-pr15)*100/pr)).round(1)
        d30 = (((pr-pr30)*100/pr)).round(1)


        ma50=(aa["50MA"][nm]).round(1)
        bbmean=(aa["30MAM"][nm]).round(1)
        ma200=(aa["200MA"][nm]).round(1)
        wh52=(aa["52WH"][nm]).round(1)
        wl52=(aa["52WL"][nm]).round(1)
        whr = (aa['WHR'][nm]).round(2)
        wlr = (aa['WLR'][nm]).round(2)

        risk=((aa["%ofL"][nm])-1).round(1)
        bubb=(aa["Bub"][nm]).round(1)
        blbb=(aa["Blb"][nm]).round(1)
        volsd=(aa["Volumesd"][nm]).round(1)
        volsdmean=(aa["Volumesdm"][nm]).round(1)
        mah50=(aa["50MAH"][nm]).round(1)
        mal50=(aa["50MAL"][nm]).round(1)
        low=(aa["Low"][nm]).round(1)
        bbr=(aa["BBR"][nm]).round(2)

        bband =  bubb - blbb
        bbandl = (((pr - blbb) / bband)*100).round(1)
        ema50 = (aa["EMA50"][nm]).round(1)
        ema50r = (aa["EMA50R"][nm]).round(2)
        bbmean=(aa["30MAM"][nm]).round(1)
        calling = (aa["Calling"][nm]).round(1)

        if calling < 0:
            macdv = -1

        if calling >= 0:
            macdv = 1
        rsi=(aa["RSI"][nm]).round(1)


        tar2 = (pr*1.02).round(0)
        tar3 = (pr*1.03).round(0)
        tar5 = (pr*1.05).round(0)






        print (i)


        B = Bought
        S = pr
        Q = QTY
        targett = Target

        print (B, Q)

        Invest = (B*Q)
        Tunrover = (B + S)* Q
        STT = Tunrover * (0.1/100)
        Tran = Tunrover * (0.00325/100)
        GST =Tran * .18
        Stamp = Tunrover * (0.015/100)
        SEBI = Tunrover * (0.002/100)
        Profit = (S - B)* Q
        NetProf = Profit - STT - Tran - GST - Stamp - SEBI
        IncomeTax = 0.3
        ActualProfit  = round(((NetProf * (1 - IncomeTax))),1)
        ActualProfitper = round((ActualProfit/Invest),2)
        print(ActualProfitper)

        total = total + ActualProfit



        if pr> Bought and pr<Target:
            symb = '^^^'

        if pr>Target:
            symb = '|||||'


        StkList.append (SymbolNS)
        BBB.append (B)
        Price.append (pr)
        ProfList.append (ActualProfit)
        ProfPList.append (ActualProfitper)
        C1D.append (d1)
        C3D.append (d3)
        C7D.append (d7)
        C10D.append (d10)
        C15D.append (d15)
        C30D.append (d30)
        WH52.append (wh52)
        WL52.append (wl52)
        WHR.append (whr)

        WLR.append (wlr)
        BBR.append (bbr)

        MACDm.append (macdv)
        BBmem.append (bbmean)

        EMA50.append(ema50)
        EMA50R.append(ema50r)
        RSI.append (rsi)
        QTYY.append (QTY)
        TAR2.append(tar2)
        TAR3.append(tar3)
        TAR5.append(tar5)
        TARGET.append(Target)

        DAYSH.append(delta)
        SYMBOL.append(symb)

        profits = profits + ActualProfit
        invests = invests + Invest
        perprofs = round(((profits/invests)*100),1)




        if hpr > Target:
            msgg = str('💚 💚 💚 💚 💚 💚') + str('\n') + str('\n')+ str('💚 SELL = ') + str(SymbolNS) + str('\n')+ str('Profit =₹') + str(ActualProfit)  + str(' (') +str(round((ActualProfitper*100),2)) + str(' %)') + str('\n')+ str('Target =₹ ') + str(Target) + str('\n') + str('Current =₹ ') + str(pr) + str('\n') + str('\n') + str('💚 💚 💚 💚 💚 💚 ')
            bot.sendMessage(chat_id, str(msgg))



# Need to defien dataframes and identify if this works. Cant do it today.

print (str("-----------------------------------------"))
print (total)
data ={'Stk^':StkList, 'Bough':BBB, 'Target':TARGET,  'Current(₹)':Price, 'Profit(₹)' : ProfList, '%Profit' : ProfPList, 'WHR':WHR, 'RSI':RSI, 'Days Held': DAYSH, 'Ind': SYMBOL }
df = pd.DataFrame(data)

print (df)
print (str("-----------------------------------------"))

writer = ExcelWriter('/home/kali/PiAuto/ProfitLoss.xlsx')



df.to_excel(writer,'ProfitLoss',index=False)


workbook  = writer.book
worksheet = writer.sheets['ProfitLoss']

writer.save()

filenameb = '/home/kali/PiAuto/ProfitLoss.xlsx'
captionn = str('P/L :₹ ')+ str(total)+ str(' (')+ str(perprofs)+ str(' %)')
bot.sendDocument(chat_id, document = open(filenameb,'rb'), caption = captionn)

