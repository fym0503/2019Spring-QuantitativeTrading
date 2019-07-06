from select_factor import get_factors
from mylib import get_data
from mylib import get_data_fromDB		#从数据库中获取数据
from mylib import train_test_split
from label_generator import generate_label
from mltool import method 
from sklearn.metrics import classification_report
import numpy  as  np

def train(high,low,dopen,close,vol,ratio,set_bool):
	BBANDS_1=False
	DEMA_1=False
	EMA_1=False
	HT_TRENDLINE_1=False
	KAMA_1=False
	MA_1=False
	MAMA_1=False
	MIDPOINT_1=False
	MIDPRICE_1=False
	SAR_1=False
	SAREXT_1=False
	SMA_1=False
	T3_1=False
	TEMA_1=False
	TRIMA_1=False
	WMA_1=False
	AD_1=False
	ADOSC_1=False
	OBV_1=False
	HT_DCPERIOD_1=False
	HT_DCPHASE_1=False
	HT_PHASOR_1=False
	HT_SINE_1=False
	HT_TRENDMODE_1=False
	AVGPRICE_1=False
	MEDPRICE_1=False
	TYPPRICE_1=False
	WCLPRICE_1=False
	ATR_1=False
	NATR_1=False
	TRANGE_1=False
	ADX_1=False
	ADXR_1=False
	APO_1=False
	AROON_1=False
	AROONOSC_1=False
	BOP_1=False
	CCI_1=False
	CMO_1=False
	DX_1=False
	MACD_1=False
	ivergence_1=False
	MACDEXT_1=False
	MACDFIX_1=False
	MFI,MINUS_DI_1=False
	MINUS_DM_1=False
	MOM_1=False
	PLUS_DI_1=False
	PLUS_DM_1=False
	PPO_1=False
	ROC_1=False
	ROCP_1=False
	ROCR_1=False
	ROCR100_1=False
	RSI_1=False
	STOCH_1=False
	STOCHF_1=False
	STOCHRSI_1=False
	TRIX_1=False
	ULTOSC_1=False
	WILLR_1=False
	if 'BBANDS' in set_bool:
		BBANDS_1=True
	if 'DEMA' in set_bool:
		DEMA_1=True
	if 'EMA' in set_bool:
		EMA_1=True
	if 'HT_TRENDLINE' in set_bool:
		HT_TRENDLINE_1=True
	if 'KAMA' in set_bool:
		KAMA_1=True
	if 'MA' in set_bool:
		MA_1=True
	if 'MAMA' in set_bool:
		MAMA_1=True
	if 'MIDPOINT' in set_bool:
		MIDPOINT_1=True
	if 'MIDPRICE' in set_bool:
		MIDPRICE_1=True
	if 'SAR' in set_bool:
		SAR_1=True
	if 'SAREXT' in set_bool:
		SAREXT_1=True
	if 'SMA' in set_bool:
		SMA_1=True
	if 'T3' in set_bool:
		T3_1=True
	if 'TEMA' in set_bool:
		TEMA_1=True
	if 'TRIMA' in set_bool:
		TRIMA_1=True
	if 'WMA' in set_bool:
		WMA_1=True
	if 'AD' in set_bool:
		AD_1=True
	if 'ADOSC' in set_bool:
		ADOSC_1=True
	if 'OBV' in set_bool:
		OBV_1=True
	if 'HT_DCPERIOD' in set_bool:
		HT_DCPERIOD_1=True
	if 'HT_DCPHASE' in set_bool:
		HT_DCPHASE_1=True
	if 'HT_PHASOR' in set_bool:
		HT_PHASOR_1=True
	if 'HT_SINE' in set_bool:
		HT_SINE_1=True
	if 'HT_TRENDMODE' in set_bool:
		HT_TRENDMODE_1=True
	if 'AVGPRICE' in set_bool:
		AVGPRICE_1=True
	if 'MEDPRICE' in set_bool:
		MEDPRICE_1=True
	if 'TYPPRICE' in set_bool:
		TYPPRICE_1=True
	if 'WCLPRICE' in set_bool:
		WCLPRICE_1=True
	if 'ATR' in set_bool:
		ATR_1=True
	if 'NATR' in set_bool:
		NATR_1=True
	if 'TRANGE' in set_bool:
		TRANGE_1=True
	if 'ADX' in set_bool:
		ADX_1=True
	if 'ADXR' in set_bool:
		ADXR_1=True
	if 'APO' in set_bool:
		APO_1=True
	if 'AROON' in set_bool:
		AROON_1=True
	if 'AROONOSC' in set_bool:
		AROONOSC_1=True
	if 'BOP' in set_bool:
		BOP_1=True
	if 'CCI' in set_bool:
		CCI_1=True
	if 'CMO' in set_bool:
		CMO_1=True
	if 'DX' in set_bool:
		DX_1=True
	if 'MACD' in set_bool:
		MACD_1=True
	if 'ivergence' in set_bool:
		ivergence_1=True
	if 'MACDEXT' in set_bool:
		MACDEXT_1=True
	if 'MACDFIX' in set_bool:
		MACDFIX_1=True
	if 'MFI,MINUS_DI' in set_bool:
		MFI,MINUS_DI_1=True
	if 'MINUS_DM' in set_bool:
		MINUS_DM_1=True
	if 'MOM' in set_bool:
		MOM_1=True
	if 'PLUS_DI' in set_bool:
		PLUS_DI_1=True
	if 'PLUS_DM' in set_bool:
		PLUS_DM_1=True
	if 'PPO' in set_bool:
		PPO_1=True
	if 'ROC' in set_bool:
		ROC_1=True
	if 'ROCP' in set_bool:
		ROCP_1=True
	if 'ROCR' in set_bool:
		ROCR_1=True
	if 'ROCR100' in set_bool:
		ROCR100_1=True
	if 'RSI' in set_bool:
		RSI_1=True
	if 'STOCH' in set_bool:
		STOCH_1=True
	if 'STOCHF' in set_bool:
		STOCHF_1=True
	if 'STOCHRSI' in set_bool:
		STOCHRSI_1=True
	if 'TRIX' in set_bool:
		TRIX_1=True
	if 'ULTOSC' in set_bool:
		ULTOSC_1=True
	if 'WILLR' in set_bool:
		WILLR_1=True
	datasets=get_factors(high=high,low=low,close=close,volume=vol,BBANDS=BBANDS_1,DEMA=DEMA_1,EMA=EMA_1,HT_TRENDLINE=HT_TRENDLINE_1,KAMA=KAMA_1,MA=MA_1,MAMA=MAMA_1,MIDPOINT=MIDPOINT_1,MIDPRICE=MIDPRICE_1,SAR=SAR_1,SAREXT=SAREXT_1,SMA=SMA_1,T3=T3_1,TEMA=TEMA_1,TRIMA=TRIMA_1,WMA=WMA_1,AD=AD_1,ADOSC=ADOSC_1,OBV=OBV_1,HT_DCPERIOD=HT_DCPERIOD_1,HT_DCPHASE=HT_DCPHASE_1,HT_PHASOR=HT_PHASOR_1,HT_SINE=HT_SINE_1,HT_TRENDMODE=HT_TRENDMODE_1,AVGPRICE=AVGPRICE_1,MEDPRICE=MEDPRICE_1,TYPPRICE=TYPPRICE_1,WCLPRICE=WCLPRICE_1,ATR=ATR_1,NATR=NATR_1,TRANGE=TRANGE_1,ADX=ADX_1,ADXR=ADXR_1,APO=APO_1,AROON=AROON_1,AROONOSC=AROONOSC_1,BOP=BOP_1,CCI=CCI_1,CMO=CMO_1,DX=DX_1,MACD=MACD_1,ivergence=ivergence_1,MACDEXT=MACDEXT_1,MACDFIX=MACDFIX_1,MFI,MINUS_DI=MFI,MINUS_DI_1,MINUS_DM=MINUS_DM_1,MOM=MOM_1,PLUS_DI=PLUS_DI_1,PLUS_DM=PLUS_DM_1,PPO=PPO_1,ROC=ROC_1,ROCP=ROCP_1,ROCR=ROCR_1,ROCR100=ROCR100_1,RSI=RSI_1)
	#train_data,test_data=train_test_split(datasets)
	label=generate_label(close,sign=1)
	#train_label,test_label=train_test_split(label)
	pred=[]
	true_value=[]
	start=int(len(datasets)*ratio)
	for i in range(start,len(datasets)-1):
		#print(datasets)
		#print(label)
		method[5].fit(datasets[:i,:],label[:i])
		
		pred.append(method[5].predict(np.array(datasets[i]).reshape(1,-1)))
		true_value.append(label[i])
	#print(classification_report(np.array(true_value),pred))
	return classification_report(np.array(true_value),pred)