import talib as ta
import numpy as np
import csv
from leave_nan import fill_nan
from mylib import normalization
from mylib import get_data
def array_process(array):
	fill_nan(array,3)
	array=array[:,np.newaxis]
	array=normalization(array)
	return array	
def get_factors(high,low,close,volume,set_bool):
	BBANDS=False
	DEMA=False
	EMA=False
	HT_TRENDLINE=False
	KAMA=False
	MA=False
	MAMA=False
	MIDPOINT=False
	MIDPRICE=False
	SAR=False
	SAREXT=False
	SMA=False
	T3=False
	TEMA=False
	TRIMA=False
	WMA=False
	AD=False
	ADOSC=False
	OBV=False
	HT_DCPERIOD=False
	HT_DCPHASE=False
	HT_PHASOR=False
	HT_SINE=False
	HT_TRENDMODE=False
	AVGPRICE=False
	MEDPRICE=False
	TYPPRICE=False
	WCLPRICE=False
	ATR=False
	NATR=False
	TRANGE=False
	ADX=False
	ADXR=False
	APO=False
	AROON=False
	AROONOSC=False
	BOP=False
	CCI=False
	CMO=False
	DX=False
	MACD=False
	ivergence=False
	MACDEXT=False
	MACDFIX=False
	MFI=False
	MINUS_DI=False
	MINUS_DM=False
	MOM=False
	PLUS_DI=False
	PLUS_DM=False
	PPO=False
	ROC=False
	ROCP=False
	ROCR=False
	ROCR100=False
	RSI=False
	STOCH=False
	STOCHF=False
	STOCHRSI=False
	TRIX=False
	ULTOSC=False
	WILLR=False
	if 'BBANDS' in set_bool:
		BBANDS=True
	if 'DEMA' in set_bool:
		DEMA=True
	if 'EMA' in set_bool:
		EMA=True
	if 'HT_TRENDLINE' in set_bool:
		HT_TRENDLINE=True
	if 'KAMA' in set_bool:
		KAMA=True
	if 'MA' in set_bool:
		MA=True
	if 'MAMA' in set_bool:
		MAMA=True
	if 'MIDPOINT' in set_bool:
		MIDPOINT=True
	if 'MIDPRICE' in set_bool:
		MIDPRICE=True
	if 'SAR' in set_bool:
		SAR=True
	if 'SAREXT' in set_bool:
		SAREXT=True
	if 'SMA' in set_bool:
		SMA=True
	if 'T3' in set_bool:
		T3=True
	if 'TEMA' in set_bool:
		TEMA=True
	if 'TRIMA' in set_bool:
		TRIMA=True
	if 'WMA' in set_bool:
		WMA=True
	if 'AD' in set_bool:
		AD=True
	if 'ADOSC' in set_bool:
		ADOSC=True
	if 'OBV' in set_bool:
		OBV=True
	if 'HT_DCPERIOD' in set_bool:
		HT_DCPERIOD=True
	if 'HT_DCPHASE' in set_bool:
		HT_DCPHASE=True
	if 'HT_PHASOR' in set_bool:
		HT_PHASOR=True
	if 'HT_SINE' in set_bool:
		HT_SINE=True
	if 'HT_TRENDMODE' in set_bool:
		HT_TRENDMODE=True
	if 'AVGPRICE' in set_bool:
		AVGPRICE=True
	if 'MEDPRICE' in set_bool:
		MEDPRICE=True
	if 'TYPPRICE' in set_bool:
		TYPPRICE=True
	if 'WCLPRICE' in set_bool:
		WCLPRICE=True
	if 'ATR' in set_bool:
		ATR=True
	if 'NATR' in set_bool:
		NATR=True
	if 'TRANGE' in set_bool:
		TRANGE=True
	if 'ADX' in set_bool:
		ADX=True
	if 'ADXR' in set_bool:
		ADXR=True
	if 'APO' in set_bool:
		APO=True
	if 'AROON' in set_bool:
		AROON=True
	if 'AROONOSC' in set_bool:
		AROONOSC=True
	if 'BOP' in set_bool:
		BOP=True
	if 'CCI' in set_bool:
		CCI=True
	if 'CMO' in set_bool:
		CMO=True
	if 'DX' in set_bool:
		DX=True
	if 'MACD' in set_bool:
		MACD=True
	if 'ivergence' in set_bool:
		ivergence=True
	if 'MACDEXT' in set_bool:
		MACDEXT=True
	if 'MACDFIX' in set_bool:
		MACDFIX=True
	if 'MFI' in set_bool:
		MFI=True
	if 'MINUS_DI' in set_bool:
		MINUS_DI=True
	if 'MINUS_DM' in set_bool:
		MINUS_DM=True
	if 'MOM' in set_bool:
		MOM=True
	if 'PLUS_DI' in set_bool:
		PLUS_DI=True
	if 'PLUS_DM' in set_bool:
		PLUS_DM=True
	if 'PPO' in set_bool:
		PPO=True
	if 'ROC' in set_bool:
		ROC=True
	if 'ROCP' in set_bool:
		ROCP=True
	if 'ROCR' in set_bool:
		ROCR=True
	if 'ROCR100' in set_bool:
		ROCR100=True
	if 'RSI' in set_bool:
		RSI=True
	if 'STOCH' in set_bool:
		STOCH=True
	if 'STOCHF' in set_bool:
		STOCHF=True
	if 'STOCHRSI' in set_bool:
		STOCHRSI=True
	if 'TRIX' in set_bool:
		TRIX=True
	if 'ULTOSC' in set_bool:
		ULTOSC=True
	if 'WILLR' in set_bool:
		WILLR=True
	fators=['BBANDS','DEMA','EMA','HT_TRENDLINE','KAMA','MA','MAMA','MIDPOINT','MIDPRICE','SAR','SAREXT','SMA','T3','TEMA','TRIMA','WMA',
	'AD','ADOSC','OBV','HT_DCPERIOD','HT_DCPHASE','HT_PHASOR','HT_SINE','HT_TRENDMODE','AVGPRICE','MEDPRICE','TYPPRICE','WCLPRICE','ATR','NATR','TRANGE',
	'ADX','ADXR','APO','AROON','AROONOSC','BOP','CCI','CMO','DX','MACD','ivergence','MACDEXT','MACDFIX','MFI','MINUS_DI','MINUS_DM','MOM','PLUS_DI','PLUS_DM','PPO','ROC','ROCP','ROCR','ROCR100','RSI','STOCH','STOCHF','STOCHRSI','TRIX','ULTOSC','WILLR']
	data_sets=np.zeros([len(high),1])
	if BBANDS==True:
		upperband, middleband, lowerband =ta.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
		upperband=array_process(upperband)
		middleband=array_process(middleband)
		lowerband=array_process(lowerband)
		data_sets=np.hstack([data_sets,upperband,middleband,lowerband])
	if DEMA==True:
		dema=ta.DEMA(close, timeperiod=30)
		dema=array_process(dema)
		data_sets=np.hstack([data_sets,dema])
	if EMA==True:
		ema=ta.EMA(close, timeperiod=30)
		ema=array_process(ema)
		data_sets=np.hstack([data_sets,ema])
	if HT_TRENDLINE==True:
		trendline=ta.HT_TRENDLINE(close)
		trendline=array_process(trendline)
		data_sets=np.hstack([data_sets,trendline])
	if KAMA==True:
		kama=ta.KAMA(close, timeperiod=30)
		kama=array_process(kama)
		data_sets=np.hstack([data_sets,kama])
	if MA==True:
		ma=ta.MA(close, timeperiod=30, matype=0)
		ma=array_process(ma)
		data_sets=np.hstack([data_sets,ma])
	if MAMA==True:
		mama, fama=ta.MAMA(close, fastlimit=0, slowlimit=0)
		mama=array_process(mama)
		fama=array_process(fama)
		data_sets=np.hstack([data_sets,mama,fama])
	if MIDPOINT==True:
		midpoint=ta.MIDPOINT(close, timeperiod=14)
		midpoint=array_process(midpoint)
		data_sets=np.hstack([data_sets,midpoint])
	if MIDPRICE==True:
		midprice=ta.MIDPRICE(high, low, timeperiod=14)
		midprice=array_process(midprice)
		data_sets=np.hstack([data_sets,midprice])
	if SAR==True:	
		sar=ta.SAR(high, low, acceleration=0, maximum=0)
		sar=array_process(sar)
		data_sets=np.hstack([data_sets,sar])
	if SAREXT==True:
		sarext=ta.SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
		sarext=array_process(sarext)
		data_sets=np.hstack([data_sets,sarext])
	if SMA==True:
		sma=ta.SMA(close, timeperiod=30)
		sma=array_process(sma)
		data_sets=np.hstack([data_sets,sma])
	if T3==True:
		t3=ta.T3(close, timeperiod=5, vfactor=0)
		t3=array_process(t3)
		data_sets=np.hstack([data_sets,t3])
	if TEMA==True:
		tema=ta.TEMA(close, timeperiod=30)
		tema=array_process(tema)
		data_sets=np.hstack([data_sets,tema])
	if TRIMA==True:
		trima=ta.TRIMA(close, timeperiod=30)
		trima=array_process(trima)
		data_sets=np.hstack([data_sets,trima])
	if WMA==True:
		wma= ta.WMA(close, timeperiod=30)
		wma=array_process(wma)
		data_sets=np.hstack([data_sets,wma])
	if AD==True:
		ad=ta.AD(high, low, close, volume)
		ad=array_process(ad)
		data_sets=np.hstack([data_sets,ad])
	if ADOSC==True:
		adosc=ta.ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)
		adosc=array_process(adosc)
		data_sets=np.hstack([data_sets,adosc]) 
	if OBV==True:
		obv=ta.OBV(close, volume)
		obv=array_process(obv)
		data_sets=np.hstack([data_sets,obv])
	if HT_DCPERIOD==True:
		dcperiod=ta.HT_DCPERIOD(close)
		dcperiod=array_process(dcperiod)
		data_sets=np.hstack([data_sets,dcperiod])
	if HT_DCPHASE==True:
		dcphase=ta.HT_DCPHASE(close)
		dcphase=array_process(dcphase)
		data_sets=np.hstack([data_sets,dcphase])
	if HT_PHASOR==True:
		inphase, quadrature =ta.HT_PHASOR(close)
		inphase=array_process(inphase)
		data_sets=np.hstack([data_sets,inphase])
		quadrature=array_process(quadrature)
		data_sets=np.hstack([data_sets,quadrature])
	if HT_SINE==True:
		sine, leadsine=ta.HT_SINE(close)
		sine=array_process(sine)
		data_sets=np.hstack([data_sets,sine])
		leadsine=array_process(leadsine)
		data_sets=np.hstack([data_sets,leadsine])
	if HT_TRENDMODE==True:
		integer=ta.HT_TRENDMODE(close)
		integer=array_process(integer)
		data_sets=np.hstack([data_sets,integer])
	if AVGPRICE==True:
		avgprice=ta.AVGPRICE(open, high, low, close)
		avgprice=array_process(avgprice)
		data_sets=np.hstack([data_sets,avgprice])
	if MEDPRICE==True:
		medprice=ta.MEDPRICE(high, low)
		medprice=array_process(medprice)
		data_sets=np.hstack([data_sets,medprice])
	if TYPPRICE==True:
		typprice=ta.TYPPRICE(high, low, close)
		typprice=array_process(typprice)
		data_sets=np.hstack([data_sets,typprice])
	if WCLPRICE==True:
		wclprice=ta.WCLPRICE(high, low, close)
		wclprice=array_process(wclprice)
		data_sets=np.hstack([data_sets,wclprice])
	if ATR==True:
		atr=ta.ATR(high, low, close, timeperiod=14)
		atr=array_process(atr)
		data_sets=np.hstack([data_sets,atr])
	if NATR==True:
		natr=ta.NATR(high, low, close, timeperiod=14)
		natr=array_process(natr)
		data_sets=np.hstack([data_sets,natr])
	if TRANGE==True:
		trange=ta.TRANGE(high, low, close)
		natr=array_process(trange)
		data_sets=np.hstack([data_sets,trange])
	if ADX==True:
		adx= ta.ADX(high, low, close, timeperiod=14)
		adx=array_process(adx)
		data_sets=np.hstack([data_sets,adx])
	if ADXR==True:
		adxr= ta.ADXR(high, low, close, timeperiod=14)
		adxr=array_process(adxr)
		data_sets=np.hstack([data_sets,adxr])
	if APO==True:
		apo= ta.APO(close, fastperiod=12, slowperiod=26, matype=0)
		apo=array_process(apo)
		data_sets=np.hstack([data_sets,apo])
	if AROON==True:
		aroondown, aroonup = ta.AROON(high, low, timeperiod=14)
		aroondown=array_process(aroondown)
		data_sets=np.hstack([data_sets,aroondown])
		aroonup=array_process(aroonup)
		data_sets=np.hstack([data_sets,aroonup])
	if AROONOSC==True:
		aroonosc= ta.AROONOSC(high, low, timeperiod=14)
		aroonosc=array_process(aroonosc)
		data_sets=np.hstack([data_sets,aroonosc])
	if BOP==True:
		bop= ta.BOP(open, high, low, close)
		bop=array_process(bop)
		data_sets=np.hstack([data_sets,bop])
	if CCI==True:
		cci= ta.CCI(high, low, close, timeperiod=14)
		cci=array_process(cci)
		data_sets=np.hstack([data_sets,cci])
	if CMO==True:
		cmo= ta.CMO(close, timeperiod=14)
		cmo=array_process(cmo)
		data_sets=np.hstack([data_sets,cmo])
	if DX==True:
		dx= ta.DX(high, low, close, timeperiod=14)
		dx=array_process(dx)
		data_sets=np.hstack([data_sets,dx])
	if MACD==True:
		macd, macdsignal, macdhist = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
		macd=array_process(macd)
		data_sets=np.hstack([data_sets,macd])
		macdhist=array_process(macdhist)
		data_sets=np.hstack([data_sets,macdhist])
		macdsignal=array_process(macdsignal)
		data_sets=np.hstack([data_sets,macdsignal])
	if MACDEXT==True:
		macd, macdsignal, macdhist = ta.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
		macd=array_process(macd)
		data_sets=np.hstack([data_sets,macd])
		macdhist=array_process(macdhist)
		data_sets=np.hstack([data_sets,macdhist])
		macdsignal=array_process(macdsignal)
		data_sets=np.hstack([data_sets,macdsignal])
	if MACDFIX==True:
		macd, macdsignal, macdhist = ta.MACDFIX(close, signalperiod=9)
		macd=array_process(macd)
		data_sets=np.hstack([data_sets,macd])
		macdhist=array_process(macdhist)
		data_sets=np.hstack([data_sets,macdhist])
		macdsignal=array_process(macdsignal)
		data_sets=np.hstack([data_sets,macdsignal])
	if MFI==True:
		mfi= ta.MFI(high, low, close, volume, timeperiod=14)
		mfi=array_process(mfi)
		data_sets=np.hstack([data_sets,mfi])
	if MINUS_DI==True:
		minus_di= ta.MINUS_DI(high, low, close, timeperiod=14)
		minus_di=array_process(minus_di)
		data_sets=np.hstack([data_sets,minus_di])
	if MINUS_DM==True:
		minus_dm= ta.MINUS_DM(high, low, timeperiod=14)
		minus_dm=array_process(minus_dm)
		data_sets=np.hstack([data_sets,minus_dm])
	if MOM==True:
		mom= ta.MOM(close, timeperiod=10)
		mom=array_process(mom)
		data_sets=np.hstack([data_sets,mom])
	if PLUS_DI==True:
		plus_di= ta.PLUS_DI(high, low, close, timeperiod=14)
		plus_di=array_process(plus_di)
		data_sets=np.hstack([data_sets,plus_di])
	if PLUS_DM==True:
		plus_dm= ta.PLUS_DM(high, low, timeperiod=14)
		plus_dm=array_process(plus_dm)
		data_sets=np.hstack([data_sets,plus_dm])
	if PPO==True:
		ppo= ta.PPO(close, fastperiod=12, slowperiod=26, matype=0)
		ppo=array_process(ppo)
		data_sets=np.hstack([data_sets,ppo])
	if ROC==True:
		roc= ta.ROC(close, timeperiod=10)
		roc=array_process(roc)
		data_sets=np.hstack([data_sets,roc])
	if ROCP==True:
		rocp= ta.ROCP(close, timeperiod=10)
		rocp=array_process(rocp)
		data_sets=np.hstack([data_sets,rocp])
	if ROCR==True:
		rocr= ta.ROCR(close, timeperiod=10)
		rocr=array_process(rocr)
		data_sets=np.hstack([data_sets,rocr])
	if ROCR100==True:
		rocr100= ta.ROCR100(close, timeperiod=10)
		rocr100=array_process(rocr100)
		data_sets=np.hstack([data_sets,rocr100])
	if RSI==True:
		rsi= ta.RSI(close, timeperiod=14)
		rsi=array_process(rsi)
		data_sets=np.hstack([data_sets,rsi])
	if STOCH==True:
		slowk, slowd = ta.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
		slowd=array_process(slowd)
		data_sets=np.hstack([data_sets,slowd])
		slowk=array_process(slowk)
		data_sets=np.hstack([data_sets,slowk])
	if STOCHF==True:
		fastk, fastd = ta.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
		fastd=array_process(fastd)
		data_sets=np.hstack([data_sets,fastd])
		fastk=array_process(fastk)
		data_sets=np.hstack([data_sets,fastk])
	if STOCHRSI==True:
		fastk, fastd = ta.STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
		fastk=array_process(fastk)
		data_sets=np.hstack([data_sets,fastk])
		fastd=array_process(fastd)
		data_sets=np.hstack([data_sets,fastd])
	if TRIX==True:
		trix= ta.TRIX(close, timeperiod=30)
		trix=array_process(trix)
		data_sets=np.hstack([data_sets,trix])
	if ULTOSC==True:	
		ultosc= ta.ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
		ultosc=array_process(ultosc)
		data_sets=np.hstack([data_sets,ultosc])
	if WILLR==True:
		willr= ta.WILLR(high, low, close, timeperiod=14)
		willr=array_process(willr)
		data_sets=np.hstack([data_sets,willr])
	return data_sets[:,1:]

