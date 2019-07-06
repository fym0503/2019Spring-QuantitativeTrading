import numpy as np
from sklearn import svm
from sklearn.metrics import classification_report
import csv
import talib as ta
import math
import pymysql
import operator
from functools import reduce

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


def get_data_fromDB(tablename):
	db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
	cursor = db.cursor()
	sql_high="""select high from """+tablename+""";"""
	cursor.execute(sql_high)	#执行sql语句
	high=cursor.fetchall()		#获取数据
	#print(high)
	high=np.array(high)			#类型转换 tuple --> array 其中tuple和array均为n维
	#print(high)
	sql_low="""select low from """+tablename+""";"""
	cursor.execute(sql_low)		#执行sql语句
	low=cursor.fetchall()
	low=np.array(low)
	sql_dopen="""select open_ from """+tablename+""";"""
	cursor.execute(sql_dopen)
	dopen=cursor.fetchall()
	dopen=np.array(dopen)
	sql_close="""select close from """+tablename+""";"""
	cursor.execute(sql_close)
	close=cursor.fetchall()
	close=np.array(close)
	sql_vol="""select volume from """+tablename+""";"""
	cursor.execute(sql_vol)
	vol=cursor.fetchall()
	vol=np.array(vol)

	#ndarry多维转换成一维
	high=np.ravel(high)
	low=np.ravel(low)
	dopen=np.ravel(dopen)
	close=np.ravel(close)
	vol=np.ravel(vol)
	
	return high,low,dopen,close,vol

def get_data_fromDB_hf(tablename):
	db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
	cursor = db.cursor()
	sql_high="""select high from """+tablename+""";"""
	cursor.execute(sql_high)	#执行sql语句
	high=cursor.fetchall()		#获取数据
	#print(high)
	high=np.array(high)			#类型转换 tuple --> array 其中tuple和array均为n维
	#print(high)
	sql_low="""select low from """+tablename+""";"""
	cursor.execute(sql_low)		#执行sql语句
	low=cursor.fetchall()
	low=np.array(low)
	sql_dopen="""select open_ from """+tablename+""";"""
	cursor.execute(sql_dopen)
	dopen=cursor.fetchall()
	dopen=np.array(dopen)
	sql_close="""select close from """+tablename+""";"""
	cursor.execute(sql_close)
	close=cursor.fetchall()
	close=np.array(close)
	sql_vol="""select volume from """+tablename+""";"""
	cursor.execute(sql_vol)
	vol=cursor.fetchall()
	vol=np.array(vol)

	high=np.ravel(high)
	low=np.ravel(low)
	dopen=np.ravel(dopen)
	close=np.ravel(close)
	vol=np.ravel(vol)
	

	return high,low,dopen,close,vol