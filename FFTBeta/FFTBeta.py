import numpy as np
import matplotlib.pyplot as plt
import csv
def get_data(filename,pos=1):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		data=[row[pos]for row in reader]
		data.pop(0)
		data=list(map(float, data))
	return data
def fft_select_rate(filename,pos=1,mode=1,alpha=0.0,beta=0.0,min_rate=0.0,max_rate=0.0,plotcurve=True):
	data=get_data(filename,pos)
	transform_fft=np.fft.fft(data)
	recover=np.fft.ifft(transform_fft)
	truncate=[]
	if mode==1:
		min_rate=np.max(np.abs(transform_fft))*alpha+np.min(np.abs(transform_fft)*(1-alpha))
		max_rate=np.max(np.abs(transform_fft))*beta+np.min(np.abs(transform_fft)*(1-beta))
	for i in transform_fft:
		if np.abs(i)>min_rate and np.abs(i)<max_rate:
			truncate.append(i)
		else:
			truncate.append(0)
	recover_truncate=np.fft.ifft(np.array(truncate))
	if plotcurve==True:
		plt.plot(recover)
		plt.plot(recover_truncate)
		plt.show()
	return recover_truncate
def fft_select_freq(filename,pos=1,mode=1,alpha=0.0,beta=0.0,min_freq_r=0.0,max_freq_r=0.0,min_freq=0.0,max_freq=0.0,plotcurve=True):
	data=get_data(filename,pos=1)
	transform_fft=np.fft.fft(data)
	recover=np.fft.ifft(transform_fft)
	truncate=[]
	if mode==1:
		min_freq=len(transform_fft)*alpha
		max_freq=len(transform_fft)*beta
	for i in range(len(transform_fft)):
		if i<max_freq and i>min_freq:
			truncate.append(transform_fft[i])
		else:
			truncate.append(0)
	recover_truncate=np.fft.ifft(np.array(truncate))
	if plotcurve==True:
		plt.plot(data)
		plt.plot(np.abs(recover_truncate))
		plt.show()
	print(np.abs(recover_truncate))
	return recover_truncate
fft_select_freq('F:\datasets\\300330.csv',alpha=0,beta=1)
