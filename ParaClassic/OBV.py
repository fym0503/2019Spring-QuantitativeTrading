import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
import matplotlib.pyplot as plt
def OBV(ts_code):
    dw = ts.get_k_data("600647")
    dw = dw[300:]
    dw.index = range(len(dw))
    obvta = ta.OBV(dw['close'].values,dw['volume'].values)
    obv=[]
    for i in range(0,len(dw)):
        if i == 0:
            obv.append(dw['volume'].values[i])
        else:
            if dw['close'].values[i]>dw['close'].values[i-1]:
                obv.append(obv[-1]+dw['volume'].values[i])
            if dw['close'].values[i]<dw['close'].values[i-1]:
                obv.append(obv[-1]-dw['volume'].values[i])
            if dw['close'].values[i]==dw['close'].values[i-1]:
                obv.append(obv[-1])
    dw['obv'] = obv
    plt.plot(dw['close'].values)
    sum=0
    total=10000
    asset=10000                   
	back_test(np.array(dw['close'].values),obv)
	'''
	for i in range(0,len(dw)-1):
        if obv[i+1]>obv[i] and dw['open'].values[i]>dw['open'].values[i+1]:
            total=total-dw['open'].values[i]*100
            sum=sum+100
            asset=dw['open'].values[i]*sum+total
        elif obv[i+1]<obv[i] and dw['open'].values[i]<dw['open'].values[i+1]:
            if sum>100:
                total=total+dw['open'].values[i]*100
                sum=sum-100
            elif sum<=100:
                total=total+dw['open'].values[i]*sum
                sum=0       
            asset=dw['open'].values[i]*sum+total
            
        print("day: "+str(i)+"sum:"+str(sum)+"total:"+str(total)+"asset:"+str(asset))
	'''
OBV("600600")
