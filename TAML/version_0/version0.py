import numpy as np
from sklearn import svm
from sklearn.metrics import classification_report
import csv
import talib as ta
import math
def generate_label(close):
	delta=[]
	delta.append(0)
	for i in range(len(close)-1):
		delta.append(close[i+1]-close[i])
	bi_delta=[]
	for i in range(len(delta)):
		if delta[i]>0:
			bi_delta.append(1)
		else:
			bi_delta.append(0)
	return delta,bi_delta
def train_test_split(array,ratio):
	train=array[0:int(ratio*len(array))]
	test=array[int(ratio*len(array)):]
	return train,test
def get_data(filename):
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		close= [row[6]for row in reader]
		close.pop(0)
		close=list(map(float, close))
		close=np.array(close)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		high= [row[4]for row in reader]
		high.pop(0)
		high=list(map(float, high))
		high=np.array(high)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		low= [row[5]for row in reader]
		low.pop(0)
		low=list(map(float, low))
		low=np.array(low)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		vol= [row[7]for row in reader]
		vol.pop(0)
		vol=list(map(float, vol))
		vol=np.array(vol)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		dopen= [row[3]for row in reader]
		dopen.pop(0)
		dopen=list(map(float, dopen))
		dopen=np.array(dopen)
	return high,low,dopen,close,vol
def normalization(array):
	return (array-np.mean(array))/np.std(array)
ratio=0.85
high,low,dopen,close,vol=get_data("F:/datasets/high_freq/000002.csv")
_,label=generate_label(close)
ad = ta.AD(high, low, close, vol)
adosc = ta.ADOSC(high, low, close, vol, fastperiod=3, slowperiod=10)
obv=ta.OBV(close,vol)
adosc,ad,obv,label=adosc[9:],ad[9:],obv[9:],label[9:]
adosc=normalization(adosc)
ad=normalization(ad)
obv=normalization(obv)
train_label,test_label=train_test_split(label,ratio)
train_adosc,test_adosc=train_test_split(adosc,ratio)
train_ad,test_ad=train_test_split(ad,ratio)
train_obv,test_obv=train_test_split(obv,ratio)
train_data=np.vstack([train_adosc,train_ad,train_obv])
test_data=np.vstack([test_adosc,test_ad,test_obv])
train_data,test_data=train_data.T,test_data.T
clf=svm.SVC()
clf.fit(train_data,train_label)
pred=clf.predict(test_data)
print(pred)
print(test_label)
print(classification_report(test_label,pred))