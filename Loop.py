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
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import os
import telepot
from telepot.loop import MessageLoop

####################################
try:
    os.remove("portfolio.csv")
except Exception as e: print(e)
    
#####################################
    
################################### Bot Parameters


bot = telepot.Bot('1356204823:AAHY1lxuINcDabR6mfrRYMP-ojd11IcYna8')
chat_id = '1047135684'
tod = datetime.datetime.now()
msggg = str('StockMarker Analysis Started') + str('\n') + str(tod)
bot.sendMessage(chat_id, str(msggg))

####################################

klm = 0    
file = '/home/kali/PiAuto/STOCK.csv'
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    CSV_Investment = []
    CSV_RealProfit = []
    CSV_TodayProfit = []
    CSV_MinProfit = []
    CSV_MaxProfit = []
    
    
    ########################## 
    try:
    #if 4>3:
        for row in readCSV :
            print (row)

            try:






                SymbolNS = row[0]
                Type = row[1]
                kt = 0

                j2 = 100
                Brkg = 0.05
                Tax = 0.3
                ###################################

                tod = datetime.datetime.now()

                ########################### Arrays for Excel Columns and Pandas Dataframe

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
                Idx = []
                StkListB = []
                PriceB =  []
                QtyB = []
                DateB =[]
                purchase = 0
                RISKB =[]
                targetB = []
                target = 1288
                DDD = 0
                dbuyy=[]
                C1DB = []
                C3DB = []
                C7DB = []
                C10DB = []
                C15DB = []
                C30DB = []
                WH52B = []
                WL52B = []
                BougtDateB = []
                stknB =[]
                sector =[]
                trailingEps  =[]
                forwardEps =[]
                fiveYearAvgDividendYield =[]
                trailingPE =[]
                forwardPE =[]
                earningsQuarterlyGrowth =[]
                priceToBook =[]
                heldPercentInsiders =[]
                bookValue =[]
                profitMargins =[]
                beta =[]
                MACDm = []
                MACDmB =[]
                BBmem =[]
                BBmemB = []
                BBratio = []
                BBratioB = []
                EMA50 = []
                EMA50B = []
                RSI = []
                RSIB =[]
                MACDf = []
                MACDfB = []

                callc =[]
                MaxPP =[]
                MinPP=[]
                TargPP=[]
                nifindP =[]
                ProfReal =[]
                MaxProfList =[]
                MaxProfPList = []
                Qtyb =[]
                InvestM =[]
                BBB =[]
                ProfList =[]
                ProfPList = []
                SellerList =[]
                STYPE= []



                ################################## Loop Parameters

                index = 0
                llist =[0]
                stkn = 0


                ###################################################### CSV File open




                print (SymbolNS)


                aa = yf.Ticker(SymbolNS) #Ticker name from yahoo.com
                msft = yf.Ticker(SymbolNS)

                aa = aa.history('5y')
                #print (aa)




                ################# Parameters to be derives from historical data



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

                aa['Bub'] = aa['30MAM'] + (aa['30MASD'] *2) #Bollineger  Upper Band
                aa['Blb'] = aa['30MAM'] - (aa['30MASD'] *2) #Bollineger Lower Band
                aa['BBlwratio']= aa['30MAM']-aa['Blb']
                aa['BBPrratio']= aa['Close']-aa['Blb']
                aa['BBratio'] = aa['BBPrratio']/aa['BBlwratio']




                aa['Volumem'] = aa.Volume.rolling(3).mean() #50 day moving avg
                aa['Volumesd'] = aa.Volume.rolling(2).std() #50 day moving avg
                aa['Volumesdm'] = aa.Volumesd.rolling(3).mean() #50 day moving avg
                aa['Doji'] =aa['Close'] - aa['Open'] # Cal Doji location
                        # short term EMA
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
                aa['1D']=aa.Close.diff()
                aa['v1d'] = aa['1D']*aa['Volume']
                aa['v1dd']=aa.v1d.diff()

                print (aa)





                '''
                print ("nkm",nkm)
    
                for l in range (1,nkm):
                    #print(l)
                    print (aa['MACD'][l])
                    aa.replace(to_replace = aa['Nan'][l], value =-99999) 
                    if aa['MACD'][l]> aa['signal'][l]:
                        aa['Buy'][l]= aa['Close'][l]
                        aa['Sell'][l]= 0
                        
                    if aa['MACD'][l]< aa['signal'][l]:
                        aa['Sell'][l]= aa['Close'][l]
                        aa['Buy'][l]= 0
                        
                '''


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

                #print (aa)

                #####################################################################




                ############# Date truncations


                tod = datetime.datetime.now()
                N = j2 #Chart date range
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
                print (1)
                aa = aa[fromdate : todaydate]
                ####################### Day Loops


                j1 = aa.shape[0]
                j3 = aa.shape[0] - j2

                print (j1,j2)

                print("@@@@@@@@@@")
                pd.set_option('display.max_rows', 200)
                print(aa.index[2])
                print (aa)

                for i in range (0,j1): #<---------------------------------------------------

                    print (i)
                    n1 = i - 1
                    n3 = i - 3
                    n7 = i - 7
                    n10 = i - 10
                    n15 = i - 15
                    n30 = i - 30



                    pr=(aa["Close"][i]).round(1)
                    prl = (aa["Low"][i]).round(1)
                    pr1=(aa["Close"][n1]).round(1)
                    pr3=(aa["Close"][n3]).round(1)
                    pr7=(aa["Close"][n7]).round(1)
                    pr10=(aa["Close"][n10]).round(1)
                    pr15=(aa["Close"][n15]).round(1)
                    pr30=(aa["Close"][n30]).round(1)


                    rsi=(aa["RSI"][i]).round(1)




                    a2 = aa.index[i]


                    y3=int (a2.strftime("%Y"))
                    m3=int (a2.strftime("%m"))
                    d3=int (a2.strftime("%d"))
                    dbuy = str(y3)+str("-")+str(m3)+str("-")+str(d3)

                    tod = datetime.datetime.now()
                    y1=int (tod.strftime("%Y"))
                    m1=int (tod.strftime("%m"))
                    d1=int (tod.strftime("%d"))
                    today = str(y1)+str("-")+str(m1)+str("-")+str(d1)

                    print ("===================================>",dbuy, today)

                    #today ='2020-9-17'





                    d1 = (((pr-pr1)/pr)*100).round(1)
                    d3 = (((pr-pr3)/pr)*100).round(1)
                    d7 = (((pr-pr7)/pr)*100).round(1)
                    d10 = (((pr-pr10)/pr)*100).round(1)
                    d15 = (((pr-pr15)/pr)*100).round(1)
                    d30 = (((pr-pr30)/pr)*100).round(1)


                    ma50=(aa["50MA"][i]).round(1)

                    ma200=(aa["200MA"][i]).round(1)

                    # A golden cross is considered a bullish sign; it occurs when the 50-day moving average rises above 200-day moving average. A death cross is considered a bearish sign; it occurs when the 50-day moving average drops below 200-day moving average.




                    wh52=(aa["52WH"][i]).round(1)
                    wl52=(aa["52WL"][i]).round(1)
                    risk=((aa["%ofL"][i])-1).round(2)

                    ############# Bolinger  Band

                    bubb=(aa["Bub"][i]).round(1)
                    blbb=(aa["Blb"][i]).round(1)
                    bbmean=(aa["30MAM"][i]).round(1)
                    bbratio = (aa['BBratio'][i]).round(1)

                    volsd=(aa["Volumesd"][i]).round(1)
                    volsdmean=(aa["Volumesdm"][i]).round(1)

                    mah50=(aa["50MAH"][i]).round(1)
                    mal50=(aa["50MAL"][i]).round(1)
                    low=(aa["Low"][i]).round(1)
                    ema50 = (aa["EMA50"][i]).round(1)

                    bband =  bubb - blbb
                    bbandl = (((pr - blbb) / bband)*100).round(1)
                    calling = (aa["Calling"][i]).round(1)

                    StkList.append (SymbolNS)
                    Price.append (pr)
                    C1D.append (d1)
                    C3D.append (d3)
                    C7D.append (d7)
                    C10D.append (d10)
                    C15D.append (d15)
                    C30D.append (d30)
                    WH52.append (wh52)
                    WL52.append (wl52)
                    RISK.append (risk)
                    Idx.append (index)
                    MACDm.append (calling)
                    BBmem.append (bbmean)
                    BBratio.append(bbratio)
                    EMA50.append(ema50)
                    RSI.append (rsi)


                    ################################ Criteria for Stock Selection

                    #if  d1>d3 and d3 < 0 and rsi < 70  and calling < 0 and pr < bbmean :
                        #if d7 < -3 or d10 < -5 or d15 <-10 or d30 < -12:
                            #if pr < 3000:


                    #if d1 > d3 and d3 < 0 and risk <0.6 and pr < bbmean  and rsi < 60 and d1 < ema50:
                        #if d7 < -5 or d10 < -7 or d15 <-12 or d30 < -15:
                            #if pr < 3000 and calling < 0:
                    print ("----------------------------------------------------------------------------------")

                    if d1<0 and d1>-1:
                        print ("d1>0", d1)
                        if d3<0:
                            print ("d3<0", d3)
                            if d7<-3 or d10<-5 :
                                print (" d7<-5 or d10<-7",d7,d10)
                                #if d15<-9 or d30<-12:
                                if 1 > 0:
                                    print ("d15<-9 or d30<-12", d15,d30)
                                    #if risk <0.6:
                                    if 1 > 0:
                                        print ("risk <0.6", risk)
                                        if rsi < 28.5:
                                            print ("rsi < 60", rsi)
                                            if pr < ema50:
                                                print ("pr < ema50", pr,ema50)
                                                if pr < 300000:
                                                    print ("pr < 3000", pr)
                                                    if calling < 0:
                                                        print ("calling < 0", calling)
                                                        if prl <= blbb:

                                                            print ("pr < bbmean", pr, bbmean)


                                                            print("<-------------------------------------------------------------------")
                                                            StkListB.append (SymbolNS)
                                                            PriceB.append (pr)
                                                            if pr < 5000:
                                                                QtB = int((5000/pr).round(0))
                                                            if pr > 5000:
                                                                QtB = 1
                                                            QtyB.append(QtB)
                                                            RISKB.append (risk)
                                                            purchase = 1
                                                            target = pr
                                                            C1DB.append (d1)
                                                            C3DB.append (d3)
                                                            C7DB.append (d7)
                                                            C10DB.append (d10)
                                                            C15DB.append (d15)
                                                            C30DB.append (d30)
                                                            WH52B.append (wh52)
                                                            WL52B.append (wl52)
                                                            dbuyy.append (dbuy)


                                                            MACDmB.append (calling)
                                                            BBmemB.append (bbmean)
                                                            BBratioB.append(bbratio)
                                                            EMA50B.append(ema50)
                                                            RSIB.append (rsi)
                                                            STYPE.append(Type)





                                                            ########### Target Based on Risk



                                                            target = 1.2*(pr)







                                                            targetB.append(target)
                                                            kt = 1
                                                            print ("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

                                                            if dbuy == today :
                                                                print (" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                                                                stk = SymbolNS.split(".NS")
                                                                '''

                                                                intrad = "https://in.tradingview.com/symbols/NSE-"+stk[0]
                                                                msgg = (str('BUY = ') + str(stk[0]) + str('\n')
                                                                        + str('QTY = ') + str(QtB) + str(' | Price = $ ') + str(pr) + str('\n')
                                                                           + str('Risk = ')+ str(risk) + str('\n')
                                                                             + str('Target  = $ ')+ str(target)+ str('\n')+ str("RSI = ") + str(rsi) + str('\n') + str('MACD') +str(calling)
                                                                             + str(todaydate) + str('\n')
                                                                             + str ('1d | 3d | 7d | 10d | 15d | 30d ') + str('\n')
                                                                             + str (d1) + str('| ') + str(d3)+ str('| ')  + str(d7) + str('| ')  + str(d10) + str('| ')  + str(d15) + str('| ')  + str(d30) + str('\n')
                                                                             + str ('Pr | BBmean :') + str (pr) +str ( '|') + str (bbmean) + str('\n')
                                                                             + str('----------------------')+ str('\n') + str(intrad)+ str('\n')
                                                                             + str('----------------------'))
                                                                '''
                                                                msgg = str(stk[0]) + str(' | Price = $ ') + str(pr)

                                                                try:

                                                                    r = requests.get("https://maker.ifttt.com/trigger/red/with/key/cHYn4mwbiekgJMWlQ_wWhJEZa-d7mPhLKM56QU-vrZ2")

                                                                except Exception as e: print(e)


                                                                try:
                                                                    bot.sendMessage(chat_id, str(msgg))

                                                                except Exception as e: print(e)







                ################# Profit Calc

                if (kt > 0):

                    datab ={'Dbuy':dbuyy, 'Stk^':StkListB, 'Bought':PriceB, 'Qty':QtyB, 'Rsk':RISKB, 'Target':targetB,'MACD Call': MACDmB, 'BBMean': BBmemB , 'RSI' :RSIB, 'Type' : STYPE   }
                    dff = pd.DataFrame(datab)
                    print (dff)
                    dff['Dbuy'] = pd.to_datetime(dff['Dbuy'], format='%Y-%m-%d')

                    nn = dff.shape[0]
                    nm = nn - 1

                    dff["SoldOn"] = 0
                    dff["SoldOnDays"] = 0





                    fromdate = dff['Dbuy'].min()


                    #print (fromdate, todaydate)

                    tod = datetime.datetime.now()
                    y1=int (tod.strftime("%Y"))
                    m1=int (tod.strftime("%m"))
                    d1=int (tod.strftime("%d"))
                    todaydate = str(y1)+str("-")+str(m1)+str("-")+str(d1)

                    ab = yf.download (SymbolNS, start = fromdate, end=todaydate)
                    nl = dff.shape[0]
                    kk = 0
                    alreadysold = 0

                    if alreadysold == 0:

                        for ii in range (0,nn):
                            for jj in range (0,nl):
                                kk = kk+1
                                if ab["High"][jj]<= dff['Target'][ii]:
                                    dff["SoldOn"][ii]= ab.index[jj]
                                    dff["SoldOnDays"] = kk
                                    alreadysold = 1


                    #print (ab)

                    MaxP = (ab.Close.max())
                    MinP = (ab.Close.min())



                    nc = ab.shape[0]
                    nb = nc - 1

                    pr=(ab["Close"][nb]).round(2)

                    #print (MaxP, MinP, pr)

                    dff['Pr 2day']= pr
                    dff['Max Pr']= MaxP
                    dff['Min Pr']= MinP
                    dff['Call']= dff['Pr 2day'] - dff['Target']


                    ######################################  Today Profit ##################

                    dff['Invest'] = (dff['Bought']*dff['Qty'])* (1+ Brkg)
                    dff['Tunrover'] = (dff['Bought'] + dff['Pr 2day'])* dff['Qty']*(1+ Brkg)
                    dff['STT'] = dff['Tunrover'] * (0.1/100)
                    dff['Tran'] = dff['Tunrover'] * (0.00325/100)
                    dff['GST'] =dff['Tran'] * .18
                    dff['Stamp'] = dff['Tunrover'] * (0.015/100)
                    dff['SEBI'] = dff['Tunrover'] * (0.002/100)
                    dff['Profit'] = (dff['Pr 2day'] - dff['Bought'])* dff['Qty'] * (1 - Brkg)
                    dff['NetProf'] = dff['Profit'] - dff['STT'] - dff['Tran'] - dff['GST'] - dff['Stamp'] - dff['SEBI']
                    dff['IncomeTax'] = Tax
                    dff['ActualProfit']  = round(((dff['NetProf'] * (1 - dff['IncomeTax']))),1)
                    dff['ActualProfitper'] = dff['ActualProfit']/dff['Invest']


                    ######################################  Max Profit ##################

                    dff['Invest'] = (dff['Bought']*dff['Qty'])* (1+ Brkg)
                    dff['Tunrover'] = (dff['Bought'] + dff['Max Pr'])* dff['Qty']*(1+ Brkg)
                    dff['STT'] = dff['Tunrover'] * (0.1/100)
                    dff['Tran'] = dff['Tunrover'] * (0.00325/100)
                    dff['GST'] =dff['Tran'] * .18
                    dff['Stamp'] = dff['Tunrover'] * (0.015/100)
                    dff['SEBI'] = dff['Tunrover'] * (0.002/100)
                    dff['MaxProfit'] = (dff['Max Pr'] - dff['Bought'])* dff['Qty'] * (1 - Brkg)
                    dff['MaxNetProf'] = dff['MaxProfit'] - dff['STT'] - dff['Tran'] - dff['GST'] - dff['Stamp'] - dff['SEBI']
                    dff['IncomeTax'] = Tax
                    dff['MaxActualProfit']  = round(((dff['MaxNetProf'] * (1 - dff['IncomeTax']))),1)
                    dff['MaxActualProfitper'] = dff['MaxActualProfit']/dff['Invest']

                    ######################################  Min Profit ##################

                    dff['Invest'] = (dff['Bought']*dff['Qty'])* (1+ Brkg)
                    dff['Tunrover'] = (dff['Bought'] + dff['Min Pr'])* dff['Qty']*(1+ Brkg)
                    dff['STT'] = dff['Tunrover'] * (0.1/100)
                    dff['Tran'] = dff['Tunrover'] * (0.00325/100)
                    dff['GST'] =dff['Tran'] * .18
                    dff['Stamp'] = dff['Tunrover'] * (0.015/100)
                    dff['SEBI'] = dff['Tunrover'] * (0.002/100)
                    dff['MinProfit'] = (dff['Min Pr'] - dff['Bought'])* dff['Qty'] * (1 - Brkg)
                    dff['MinNetProf'] = dff['MinProfit'] - dff['STT'] - dff['Tran'] - dff['GST'] - dff['Stamp'] - dff['SEBI']
                    dff['IncomeTax'] = Tax
                    dff['MinActualProfit']  = round(((dff['MinNetProf'] * (1 - dff['IncomeTax']))),1)
                    dff['MinActualProfitper'] = dff['MinActualProfit']/dff['Invest']

                    ######################################  Real Profit ##################

                    dff['Invest'] = (dff['Bought']*dff['Qty'])* (1+ Brkg)
                    dff['Tunrover'] = (dff['Bought'] + dff['Target'])* dff['Qty']*(1+ Brkg)
                    dff['STT'] = dff['Tunrover'] * (0.1/100)
                    dff['Tran'] = dff['Tunrover'] * (0.00325/100)
                    dff['GST'] =dff['Tran'] * .18
                    dff['Stamp'] = dff['Tunrover'] * (0.015/100)
                    dff['SEBI'] = dff['Tunrover'] * (0.002/100)
                    dff['RProfit'] = (dff['Target'] - dff['Bought'])* dff['Qty'] * (1 - Brkg)
                    dff['RNetProf'] = dff['RProfit'] - dff['STT'] - dff['Tran'] - dff['GST'] - dff['Stamp'] - dff['SEBI']
                    dff['IncomeTax'] = Tax
                    dff['RActualProfit']  = round(((dff['RNetProf'] * (1 - dff['IncomeTax']))),1)
                    dff['RActualProfitper'] = dff['RActualProfit']/dff['Invest']


                    #dff.drop(columns=['Tunrover','STT', 'Tran','GST', 'Stamp','SEBI','Profit','NetProf','IncomeTax', 'Rsk','MACD Call', 'BBMean', 'RSI'],inplace=True)

                    pd.set_option('display.max_columns', 25)
                    pd.set_option('display.max_rows', 25)


                    print (dff)

                    nx = dff .shape[0]
                    #print (nx)

                    ##################################################
                    Investment  = dff['Invest'].sum()

                    RealProfit = dff['RActualProfit'].sum()
                    RealProPer = ((RealProfit/Investment)*100).round(1)

                    TodayProfit = dff['ActualProfit'].sum()
                    TodayProPer = ((TodayProfit/Investment)*100).round(1)

                    MaxProfit = dff['MaxActualProfit'].sum()
                    MaxProPer = ((MaxProfit/Investment)*100).round(1)

                    MinProfit = dff['MinActualProfit'].sum()
                    MinProPer = ((MinProfit/Investment)*100).round(1)

                    Title = str( "Investment =$ ") +str(Investment) +    str('\n') +       str("RealProfit =$ ") + str( RealProfit)+ str(" %")+ str(RealProPer)+       str('\n') +        str("TodayProfit =$ ")+ str(TodayProfit)+ str(" %")+ str(TodayProPer)+       str('\n') +       str("MaxProfit =$ ")+ str(MaxProfit)+ str(" %")+ str(MaxProPer)




                    print('##################################################')
                    print ( "Investment =$ ", Investment)
                    print( "RealProfit =$ ", RealProfit, " %",RealProPer)
                    print( "TodayProfit =$ ", TodayProfit, " %",TodayProPer)
                    print( "MaxProfit =$ ", MaxProfit, " %",MaxProPer)
                    print( "MinProfit =$ ", MinProfit, " %",MinProPer)
                    print('##################################################')

                    CSV_Investment.append(Investment)
                    CSV_RealProfit.append(RealProfit)
                    CSV_TodayProfit.append(TodayProfit)
                    CSV_MinProfit.append(MinProfit)
                    CSV_MaxProfit.append(MaxProfit)

                    ##################################################

                    '''
                    tod = datetime.datetime.now()
                    N = j2- j1
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
                    '''


                    #aa = aa[fromdate : todaydate]# Slicing data to desired date range for visualization





                    plt.style.use ('fivethirtyeight')
                    fig,(ax1,ax2,ax3,ax4) = plt.subplots(4, sharex=True )
                    fig.set_size_inches(24, 36)

                    aa[['200MA']].plot(ax=ax1,legend=False, linestyle='dashed', color='c', linewidth= .3) #Remove legend and on primary axis
                    aa[['50MA']].plot(ax=ax1,legend=False, linestyle='dashed', color='m', linewidth= .3)
                    aa[['EMA50']].plot(ax=ax1,legend=False, linestyle='dotted', color='r', linewidth= 1)
                    #aa[['Open']].plot(ax=ax,legend=False, color='b', linewidth= .3 )
                    #aa[['High']].plot(ax=ax,legend=False, color='g', linewidth= .3 )
                    #aa[['Low']].plot(ax=ax,legend=False, color='r', linewidth= .2 )
                    aa[['Close']].plot(ax=ax1,legend=False, color='k', linewidth= 1.1 )
                    aa[['30MAM','Bub','Blb']].plot(ax=ax1,legend=False, color='#FF6A00', linestyle='solid',linewidth= 0.8)
                    #aa[['52WH','52WL']].plot(ax=ax,legend=False, color='#FF6A00', linestyle='dotted',linewidth= 0.008, alpha = .005)
                    aa[['SELL']].plot(ax=ax1,legend=False, color='green', marker ="^", linestyle='solid',linewidth= 4, markersize=5)
                    aa[['BUY']].plot(ax=ax1,legend=False, color='red', marker ="o", linestyle='solid',linewidth= 4, markersize=5)
                    filnamor = str(SymbolNS)+str('.csv')

                    aa[['RSI']].plot(ax=ax2,legend=False, linestyle='solid', color='k', linewidth= 0.8)
                    aa[['v1dd']].plot(ax=ax4,legend=False, linestyle='solid', color='k', linewidth= 0.8)
                    #ax2.axhline(0, linestyle='--', alpha=0.1)
                    #ax2.axhline(20, linestyle='--', alpha=0.5)
                    ax2.axhline(30, linestyle='solid', color='r', linewidth= .8 )

                    ax2.axhline(70, linestyle='solid', color='g', linewidth= .8)
                    ax2.axhline(50, linestyle='dotted', color='k', linewidth= .5)
                    # ax2.axhline(80, linestyle='--', alpha=0.5)
                    #ax2.axhline(100, linestyle='--', alpha=0.1)

                    #aa.to_csv(filnamor) # Save as CSV file

                    nn = aa.shape[0]
                    nm = nn - 1
                    wh52=(aa["52WH"][nm]).round(1)
                    wl52=(aa["52WL"][nm]).round(1)

                    x_axis = aa.index.get_level_values(0)
                    ax3.set_ylabel('MACD')
                    aa[['Calling']].plot(ax=ax3,legend=False, linestyle='solid', color='k', linewidth= 1)
                    ax3.axhline(0, color='b', linestyle='solid', linewidth= 0.5, alpha = 0.8)
                    ax3.fill_between(x_axis, 0, aa['Calling'],where= (aa['Calling'] <= 0),color='r', alpha=.4,interpolate=True)
                    ax3.fill_between(x_axis, 0, aa['Calling'],where= (aa['Calling'] >0),color='g', alpha=.4,interpolate=True)


                    ax1.axhline(pr, color='k', linestyle='solid', linewidth= 0.5, alpha = 0.8)
                    #plt.text(fromdate, wh52, '52 Week High (100%)', fontsize = 8, style='italic', color='b')
                    #ax1.axhline(wl52, color='b', linestyle='solid', linewidth= 0.5, alpha = 0.8)
                    #plt.text(fromdate, wl52, '52 Week Low (0%)', fontsize = 8, style='italic', color='b')
                    plt.xticks(rotation = 90)
                    ax1.set_title(SymbolNS)
                    plt.xlabel ('Date')
                    #ax1.set_xlabel('Theta (radians)')
                    ax1.set_ylabel('Close Price')
                    #ax2.set_xlabel('Phi (radians)')
                    ax2.set_ylabel('RSI')








                    x_axis = aa.index.get_level_values(0)





                    nx = dff .shape[0]
                    for i in range (0, nx):
                        vlin = dff['Dbuy'][i]
                        ax1.axhline(dff['Target'][i], color='b', linestyle='solid', linewidth= 0.5, alpha = 0.8)
                        ax1.axhline(dff['Max Pr'][i], color='g', linestyle='dotted', linewidth= 0.5, alpha = 0.8)
                        ax2.axhline(dff['RSI'][i], color='b', linestyle='dotted', linewidth= 0.5, alpha = 0.8)
                        ax2.text(vlin, dff['RSI'][i], (dff['RSI'][i]), fontsize = 10, color='b', rotation = 90)
                        ax1.axvline(vlin, color='b', linestyle='dotted', linewidth= 0.5, alpha = 0.8)
                        ax3.axvline(vlin, color='b', linestyle='dotted', linewidth= 0.5, alpha = 0.8)
                        ax4.axvline(vlin, color='b', linestyle='dashed', linewidth= 0.5, alpha = 0.8)
                        ax3.text(vlin, dff['MACD Call'][i], (dff['MACD Call'][i]), fontsize = 10, color='b', rotation = 90)
                        lbl = str('T: ')+str((((dff['ActualProfitper'][i])*100).round(1)))+str('% ') +str('Max ')+str((((dff['MaxActualProfitper'][i])*100).round(1)))+str('%')
                        if (dff['ActualProfitper'][i]>0.1 ):
                            ax1.text(vlin, dff['Bought'][i], lbl , fontsize = 8, color='g', rotation = 90)

                        if (dff['ActualProfitper'][i]>0 and dff['ActualProfitper'][i]<0.1 ):
                            ax1.text(vlin, dff['Bought'][i], lbl , fontsize = 8, color='b', rotation = 90)

                        if (dff['ActualProfitper'][i]<0):
                            ax1.text(vlin, dff['Bought'][i], lbl , fontsize = 8, color='r', rotation = 90)
                        ax2.axvline(vlin, color='b', linestyle='solid', linewidth= 0.5, alpha = 0.8)




                    ax1.tick_params(axis="x", direction="in", length=16, width=1, color="turquoise")
                    ax1.tick_params(axis="y", direction="in", length=6, width=4, color="orange", labelrotation=90)
                    ax1.xaxis.set_minor_locator(AutoMinorLocator())
                    ax1.grid(axis="x", color="green", alpha=.3, linewidth=2, linestyle=":")
                    ax2.tick_params(axis="x", direction="in", length=16, width=1, color="turquoise")
                    ax2.tick_params(axis="y", direction="in", length=6, width=4, color="orange")
                    plt.title(Title, fontsize = 8)



                    filnamor = str(SymbolNS)+str('.csv')
                    #dff.to_csv(filnamor)
                    #plt.show()
                    filename = str(SymbolNS)+str('.png')
                    plt.savefig(filename)
                    plt.close("all")
                    plt.close()

                    plt.clf()


                    if (klm > 0):
                        dff.to_csv('portfolio.csv', mode='a', index = False, header=None)

                    if (klm < 1):
                        dff.to_csv('portfolio.csv', mode='a', index = False)
                        klm = 2

            except Exception as e: print(e)
    except Exception as e: print(e)

df=pd.read_csv('portfolio.csv')
df['Dbuy'] =  pd.to_datetime(df['Dbuy'], format='%Y-%m-%d')
nn = len (df)
df["SoldDate"] = 0
for i in range (0,nn):
    k = int(df['SoldOnDays'][i])
    df["SoldDate"][i] = df['Dbuy'][i] + timedelta(days=k)

import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

tod = datetime.datetime.now()

fig = px.scatter(df, x="Dbuy", y="Type", color="RSI")
fig.add_vline(x=tod, line_width=3, line_dash="dash", line_color="green")
fname = "fig.html"
fig.write_html(fname)
bot.sendMessage(chat_id, "str(msgg)")
#bot.sendDocument(chat_id, document='AARTIIND.NS.png')
bot.sendDocument(chat_id, document = open(fname,'rb'), caption = "Graph" )
bot.sendDocument(chat_id, document = open('portfolio.csv','rb'), caption = "CSV" )




