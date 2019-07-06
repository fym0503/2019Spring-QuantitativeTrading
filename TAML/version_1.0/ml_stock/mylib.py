import numpy as np
from sklearn import svm
from sklearn.metrics import classification_report
import csv
import talib as ta
import math
def train_test_split(array,ratio=0.8):
	train=array[0:int(ratio*len(array))]
	test=array[int(ratio*len(array)):]
	return train,test
def get_data(filename):
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		close= [row[3]for row in reader]
		close.pop(0)
		close=list(map(float, close))
		close=np.array(close)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		high= [row[2]for row in reader]
		high.pop(0)
		high=list(map(float, high))
		high=np.array(high)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		low= [row[4]for row in reader]
		low.pop(0)
		low=list(map(float, low))
		low=np.array(low)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		vol= [row[5]for row in reader]
		vol.pop(0)
		vol=list(map(float, vol))
		vol=np.array(vol)
	with open(filename,'r') as csvfile:
		reader = csv.reader(csvfile)
		dopen= [row[1]for row in reader]
		dopen.pop(0)
		dopen=list(map(float, dopen))
		dopen=np.array(dopen)
	return high,low,dopen,close,vol
def normalization(array):
	return (array-np.mean(array))/np.std(array)
