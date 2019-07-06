import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
from matplotlib import rc
def MACD(ts_code,upper,lower,fastperiod=12, slowperiod=26, signalperiod=9):
    dw = ts.get_k_data(ts_code)
    close = dw.close.values
    dw['macd'], dw['macdsignal'], dw['macdhist'] = ta.MACD(close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
    macd=np.array(dw['macd'].values)
    macd=macd[33:]
    dw=dw[33:]
    sum=0
    total=10000
    asset=10000
    print(macd)
    for i in range(0,len(dw)):
        if  macd[i]>upper and sum<1000:
            total=total-dw['open'].values[i]*100
            sum=sum+100
            asset=dw['open'].values[i]*sum+total
        elif macd[i]<lower:
            if sum>100:
                total=total+dw['open'].values[i]*100
                sum=sum-100
            elif sum<=100:
                total=total+dw['open'].values[i]*sum
                sum=0       
            asset=dw['open'].values[i]*sum+total

        print("day: "+str(i)+"sum:"+str(sum)+"total:"+str(total)+"asset:"+str(asset))
