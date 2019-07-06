from select_factor import get_factors
from mylib import get_data
from mylib import train_test_split
from label_generator import generate_label
from mltool import method 
from sklearn.metrics import classification_report
filename='E:/300354.csv'
high,low,dopen,close,vol=get_data(filename)
datasets=get_factors(high,low,close,vol,BBANDS=True,DEMA=True,EMA=True,AD=True,ADOSC=True,OBV=True)
train_data,test_data=train_test_split(datasets)
label=generate_label(close,sign=1)
train_label,test_label=train_test_split(label)
method.fit(train_data,train_label)
pred=method.predict(test_data)
print(classification_report(test_label,pred))