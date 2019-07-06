import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
import matplotlib.pyplot as plt
def BBANDS(ts_code,timeperiod=14,k=0.5):
    dw = ts.get_k_data(ts_code)
    dw = dw[10:]
    dw.index = range(len(dw))
    dw['upper'], dw['middle'], dw['lower'] = ta.BBANDS(
                    dw.close.values, 
                    timeperiod=timeperiod,
                    # number of non-biased standard deviations from the mean
                    nbdevup=k,
                    nbdevdn=k,
                    # Moving average type: simple moving average here
                    matype=0)
    sum=0
    total=10000
    asset=10000
    plt.plot(dw['open'].values)
    plt.show()
    for i in range(0,len(dw)-1):
        if dw['open'].values[i]<dw['lower'].values[i]:
            total=total-dw['open'].values[i]*100
            sum=sum+100
            asset=dw['open'].values[i]*sum+total
        elif dw['open'].values[i]>dw['upper'].values[i]:
            if sum>100:
                total=total+dw['open'].values[i]*100
                sum=sum-100
            elif sum<=100:
                total=total+dw['open'].values[i]*sum
                sum=0
            asset=dw['open'].values[i]*sum+total
        print("day: "+str(i)+"sum:"+str(sum)+"total:"+str(total)+"asset:"+str(asset))
    print("total:"+str(total)+" K: "+str(k))
BBANDS("600848",k=0.5)
#for k in range(1,10):
#BBANDS("600600",k=k)#