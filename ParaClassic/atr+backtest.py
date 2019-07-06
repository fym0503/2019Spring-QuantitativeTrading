def buy_condition(i,value,args):
	#print(args)
	return value[i]-value[i-1]>1.5*args[i-1]
def sell_condition(i,value,args):
	return value[i]-value[i-1]<0.8*args[i-1]
def back_testing(value,args,total=10000,sum=0,asset=10000):
	for i in range(1,len(value)):
		if buy_condition(i,value,args) and total>0:
			if total>1000:
				total=total-1000
				sum=sum+1000.0/value[i]
			elif total<=1000:
				total=0
				sum=sum+total/value[i]
		if sell_condition(i,value,args) and sum>0:
			sum=sum/2
			total=total+sum*value[i]
		asset=total+sum*value[i]
		print("day: "+str(i)+"	stock:"+str(sum)+" cash:"+str(total)+" asset:"+str(asset))
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
import matplotlib.pyplot as plt
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
	back_testing(np.array(dw['high'].values),np.array(dw['atr'].values))
ATR("600333")
