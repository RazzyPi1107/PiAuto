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
import csv
import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import os
import telepot
from telepot.loop import MessageLoop
from mpl_toolkits import mplot3d
import seaborn as sns
df = pd.read_csv('temp.csv', header=None, names=['Time', 'Temp'])
print (df)

plt.style.use('classic')
fig,(ax) = plt.subplots(1, sharex=True )
fig.set_size_inches(21.4, 13.2)
plt.xlabel('Time')
plt.ylabel('Temp')
#plt.scatter( x=df['Time'], y=df['Temp'])

plt.xticks(rotation = 90, ha = 'right')
sns.scatterplot(data=df, x="Time", y="Temp", hue="Temp")


plt.savefig('heatmap.png', bbox_inches='tight')



# show plot
plt.show()
