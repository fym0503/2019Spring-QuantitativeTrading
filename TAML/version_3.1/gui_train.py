from select_factor import get_factors
from mylib import get_data
from mylib import get_data_fromDB		#从数据库中获取数据
from mylib import train_test_split
from label_generator import generate_label
from mltool import method 
from sklearn.metrics import classification_report
import numpy  as  np

def train(high,low,dopen,close,vol,ratio,set_bool,methodss):
	datasets=get_factors(high,low,close,vol,set_bool)
	#train_data,test_data=train_test_split(datasets)
	label=generate_label(close,sign=1)
	methods=["DecisionTreeClassifier","MLPClassifier","KNeighborsClassifier","AdaBoostClassifier","RandomForestClassifier","GradientBoostingClassifier"]
	for i in range(len(methods)):
		if methodss==methods[i]:
			num=i
	#train_label,test_label=train_test_split(label)
	pred=[]
	true_value=[]
	start=int(len(datasets)*ratio)
	for i in range(start,len(datasets)-1):
		#print(datasets)
		#print(label)
		method[num].fit(datasets[:i,:],label[:i])
		
		pred.append(method[num].predict(np.array(datasets[i]).reshape(1,-1)))
		true_value.append(label[i])
	#print(classification_report(np.array(true_value),pred))
	return classification_report(np.array(true_value),pred)