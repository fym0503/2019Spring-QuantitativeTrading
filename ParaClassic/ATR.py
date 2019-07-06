import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
import matplotlib.pyplot as plt
def ATR(ts_code,timeperiod=14,alpha=1.0,beta=1.0):
    dw = ts.get_k_data(ts_code)
    dw = dw[300:]
    dw.index = range(len(dw))
    dw['atr'] = ta.ATR(dw.high.values,dw.low.values,dw.close.values, timeperiod=timeperiod)
    total=10000
    sum=0
    for i in range(14,len(dw)-1):
        if dw.high.values[i+1]-dw.high.values[i]>alpha*dw['atr'][i]:
            total=total-dw['open'].values[i]*100
            sum=sum+100
        elif dw.high.values[i]-dw.high.values[i+1]>beta*dw['atr'][i]:
            if sum>100:
                total=total+dw['open'].values[i]*100
                sum=sum-100
            elif sum<=100:
                total=total+dw['open'].values[i]*sum
                sum=0        
    print("total:"+str(total)+" alpha :"+str(alpha)+" beta :"+str(beta))
for alpha in [0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]:
    for beta in [0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]:
        ATR("600600",alpha=alpha,beta=beta)
