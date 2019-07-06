import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt
def RSI(ts_code,upper,lower):
    dw = ts.get_k_data(ts_code)
    dw = dw[300:]
    dw.index = range(len(dw))
    close = dw.close.values
    dw["rsi"] = ta.RSI(close, timeperiod=14)
    print(dw['rsi'])
    value=np.array(dw['rsi'].values)
    value=value[14:]
    print(value)
    dw=dw[14:]
    sum=0
    total=10000
    asset=10000
    for i in range(0,len(dw)-1):
        if  value[i]<lower:
            total=total-dw['open'].values[i]*100
            sum=sum+100
            asset=dw['open'].values[i]*sum+total
        elif value[i]>upper:
            if sum>100:
                total=total+dw['open'].values[i]*100
                sum=sum-100
            elif sum<=100:
                total=total+dw['open'].values[i]*sum
                sum=0       
            asset=dw['open'].values[i]*sum+total

        print("day: "+str(i)+"sum:"+str(sum)+"total:"+str(total)+"asset:"+str(asset))