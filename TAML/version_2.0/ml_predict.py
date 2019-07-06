from select_factor import get_factors
from mylib import get_data
from mylib import get_data_fromDB       #从数据库中获取数据
from mylib import train_test_split
from label_generator import generate_label
from mltool import method 
from sklearn.metrics import classification_report

filename='E:/300354.csv'            #使用文件
tablename='stock_'+'300354'         #使用数据库
#high,low,dopen,close,vol=get_data(filename)
high,low,dopen,close,vol=get_data_fromDB(tablename)  #high类型: ndarry 维数1
datasets=get_factors(high,low,close,vol,BBANDS=True,DEMA=True,EMA=True,AD=True,ADOSC=True,OBV=True)
train_data,test_data=train_test_split(datasets)
label=generate_label(close,sign=1)
train_label,test_label=train_test_split(label)
method[5].fit(train_data,train_label)
pred=method[5].predict(test_data)
print(classification_report(test_label,pred))