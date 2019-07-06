def fft_select_freq(stock_data,high=0.7,low=0.0):
	#stock_data即原始股票数据
    transform_fft=np.fft.fft(stock_data)
    #recover即经过FFT变换后再进行逆变换得到的数据，原则上讲与原始数据相同。
	recover=np.fft.ifft(transform_fft)
	truncate=[]
    #min_freq即下截止频率。low一般设为0。
	min_freq=len(transform_fft)*low
    #max_freq即上截止频率。high一般取0.5-0.9之间的值。
	max_freq=len(transform_fft)*high
	for i in range(len(transform_fft)):
    #满足在截止频率范围内的值可以留下
		if i<max_freq and i>min_freq:
			truncate.append(transform_fft[i])
    #过于高频的部分被屏蔽清零
		else:
			truncate.append(0)
    #truncate经过逆变换后的信号是一个频率较低的信号
	recover_truncate=np.fft.ifft(np.array(truncate))
def fft_select_weight(stock_data,para_1=0.2,para_2=1.0):
    #stock_data即原始股票数据
    transform_fft=np.fft.fft(stock_data)
    #recover即经过FFT变换后再进行逆变换得到的数据，原则上讲与原始数据相同。
	recover=np.fft.ifft(transform_fft)
	truncate=[]
    #min_weight即下截止权重,para_1一般取0.1-0.5。
    min_weight=np.max(np.abs(transform_fft))*para_1+np.min(np.abs(transform_fft)*(1-para_1))
    #max_weight即下截止权重,para_1一般取1.0。
	max_weight=np.max(np.abs(transform_fft))*para_2+np.min(np.abs(transform_fft)*(1-para_2))
	for i in transform_fft:
    #权重较大的频率分量可以留下
		if np.abs(i)>min_weight and np.abs(i)<max_weight:
			truncate.append(i)
    #权重较低的频率部分被直接屏蔽为0
		else:
			truncate.append(0)
    #truncate经过逆变换后的信号是一个周期更明显的信号
	recover_truncate=np.fft.ifft(np.array(truncate))