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


#filenameb = '/home/kali/PiAuto/ProfitLoss.xlsx'

df = pd.read_excel("/home/kali/PiAuto/ProfitLoss.xlsx")

nn =  len (df)

for i in range (0,nn):
    delta =  round (((df["Target"][i] - df["Current(₹)"][i] )*100 / df["Current(₹)"][i] ),1)
    msgk = str("Name: ") + str(df["Stk^"][i]) + str('\n') + str("Bought:(₹)") + str(df["Bough"][i]) + str('\n') + str("Target:(₹)") + str(df["Target"][i]) + str('\n') + str("Today:(₹)") + str(df["Current(₹)"][i]) + str('\n') + str("%: ") + str(delta) + str('\n')
    bot.sendMessage(chat_id, str(msgk))




