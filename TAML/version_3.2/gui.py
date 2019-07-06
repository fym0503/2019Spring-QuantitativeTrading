# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mylib import get_data
from mylib import get_data_fromDB
from mylib import get_data_fromDB_hf
from mylib import train_test_split
from label_generator import generate_label
from mltool import method 
from sklearn.metrics import classification_report
import numpy  as  np
from gui_train import train
class filedialogdemo(QMainWindow):
	def __init__(self,parent=None):
		super(filedialogdemo,self).__init__(parent)
		self.resize(1600,1200)						  #大小
		self.center()
		# self.status = self.statusBar()
		# self.status.showMessage("状态栏提示",1000)	 #参数为时间
		# self.setWindowIcon(QIcon('icon.JPG'))		#图标
		self.setWindowTitle("TAML")
		self.fators = ['BBANDS','DEMA','EMA','HT_TRENDLINE','KAMA','MA','MAMA','MIDPOINT','MIDPRICE','SAR','SAREXT','SMA','T3','TEMA','TRIMA','WMA',
		'AD','ADOSC','OBV','HT_DCPERIOD','HT_DCPHASE','HT_PHASOR','HT_SINE','HT_TRENDMODE','AVGPRICE','MEDPRICE','TYPPRICE','WCLPRICE','ATR','NATR','TRANGE',
		'ADX','ADXR','APO','AROON','AROONOSC','BOP','CCI','CMO','DX','MACD','ivergence','MACDEXT','MACDFIX','MFI','MINUS_DI','MINUS_DM','MOM','PLUS_DI','PLUS_DM','PPO','ROC','ROCP','ROCR','ROCR100','RSI','STOCH','STOCHF','STOCHRSI','TRIX','ULTOSC','WILLR']
		self.canshu_new = set()			##已选参数
		self.method = ""				##已选方法

		####日期选择、代码
		self.ticker_lab = QLabel("股票代码")
		self.date_labl1 = QLabel("起始日期(2018.1.1后)")
		self.date_labl2 = QLabel("截至日期(2019.5.1前)")
		self.ratio_lab = QLabel("ratio(0-1)")
		# self.canshu_lab = QLabel("选择参数")
		self.tickerEdit = QLineEdit()
		self.tickerEdit.setValidator(QIntValidator())
		self.tickerEdit.setMaxLength(6)
		
		self.DateEdit1 = QDateTimeEdit(QDateTime.currentDateTime(),self)
		self.DateEdit1.setDisplayFormat("yyyy-MM-dd")
		self.DateEdit1.setCalendarPopup(True)
		##调用:  self.DateEdit1.date().year() self.DateEdit1.date().month()  self.DateEdit1.date().day()
		self.DateEdit2 = QDateTimeEdit(QDateTime.currentDateTime(),self)
		self.DateEdit2.setDisplayFormat("yyyy-MM-dd")
		self.DateEdit2.setCalendarPopup(True)
		self.ratioEdit = QLineEdit()
		self.ratioEdit.setValidator(QDoubleValidator(0.00000,1.00000,5))
		layout_date = QFormLayout()
		layout_date.addRow(self.ticker_lab,self.tickerEdit)
		layout_date.addRow(self.ratio_lab,self.ratioEdit)
		layout_date.addRow(self.date_labl1,self.DateEdit1)
		layout_date.addRow(self.date_labl2,self.DateEdit2)
		print(layout_date)
		####输出
		self.print_btn = QPushButton("输出:")
		self.print_btn.clicked.connect(self.out_data)
		self.texEdit = QTextEdit()
		self.texEdit.setReadOnly(True)
		self.texEdit.setFont(QFont("",10))		   #字体
		layout_print = QFormLayout()
		layout_print.addRow(self.print_btn,self.texEdit)
		
		###参数选择
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(13)
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setHorizontalHeaderLabels(['参数选择','单击取消','','',''])	 #表格头
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.init_table()
		self.tableWidget.itemClicked.connect(self.canshu_fun_new)
		layout_table = QHBoxLayout()
		layout_table.addWidget(self.tableWidget)

		###方法选择
		layout_method = QVBoxLayout()
		layout_method.addWidget(QLabel("请选择方法"))
		self.method_1 = QRadioButton("DecisionTreeClassifier")
		self.method_1 .toggled.connect(lambda:self.method_fun(self.method_1))
		layout_method.addWidget(self.method_1)
		self.method_2 = QRadioButton("MLPClassifier")
		self.method_2 .toggled.connect(lambda:self.method_fun(self.method_2))
		layout_method.addWidget(self.method_2)
		self.method_3 = QRadioButton("KNeighborsClassifier")
		self.method_3 .toggled.connect(lambda:self.method_fun(self.method_3))
		layout_method.addWidget(self.method_3)
		self.method_4 = QRadioButton("AdaBoostClassifier")
		self.method_4 .toggled.connect(lambda:self.method_fun(self.method_4))
		layout_method.addWidget(self.method_4)
		self.method_5 = QRadioButton("RandomForestClassifier")
		self.method_5 .toggled.connect(lambda:self.method_fun(self.method_5))
		layout_method.addWidget(self.method_5)
		self.method_6 = QRadioButton("GradientBoostingClassifier")
		self.method_6 .toggled.connect(lambda:self.method_fun(self.method_6))
		layout_method.addWidget(self.method_6)

		##主布局
		layout = QGridLayout()
		layout.addLayout(layout_date,0,0,2,2)
		layout.addLayout(layout_method,2,0,2,2)
		layout.addLayout(layout_table,0,2,7,8)
		layout.addLayout(layout_print,7,0,3,10)
		
		main_frame = QWidget()
		main_frame.setLayout(layout)
		self.setCentralWidget(main_frame)

	##########这里是输出
	def out_data(self):
		stock_num=self.tickerEdit.text()  #调用股票代码
		stock_name='stock_'+stock_num

		
		hf_stock_name='highfreq_stock_'+stock_num
		#high,low,dopen,close,vol=get_data_fromDB(stock_name)
		high,low,dopen,close,vol=get_data_fromDB_hf(hf_stock_name)   #高频数据

		if self.DateEdit1.date().year() == 2018:
			start_month=self.DateEdit1.date().month()  
		else:
			start_month=self.DateEdit1.date().month() + 12
		start_day=self.DateEdit1.date().day()
		if self.DateEdit2.date().year() == 2018:
			end_month=self.DateEdit2.date().month()  
		else:
			end_month=self.DateEdit2.date().month() + 12	 
		end_day=self.DateEdit2.date().day()
		#print(start_month,start_day)
		'''
		data_end=342-20*(start_month-1)
		data_start=342-20*(end_month-1)
		#print(high[data_start:data_end])
		'''
		data_end=482
		data_start=0		##高频数据时不根据输入日期选择数据

		high_train=high[data_start:data_end]
		low_train=low[data_start:data_end]
		dopen_train=dopen[data_start:data_end]
		close_train=close[data_start:data_end]
		vol_train=vol[data_start:data_end]
		set_bool=self.canshu_new
		ratio=float(self.ratioEdit.text())
		#print(ratio)
		#print(set_bool)
		print(high_train)
		out=train(high_train,low_train,dopen_train,close_train,vol_train,ratio,set_bool,self.method)








		#print(high)
		##这里参数传递 或者放在init里也可以,输出放在下面括号里即可
		self.texEdit.setPlainText(out)
		return

	def init_table(self):
		i = 0
		for a in self.fators:
			newItem = QTableWidgetItem(a)
			self.tableWidget.setItem(i//5,i%5,newItem)
			i = i+1
		return
	
	def canshu_fun_new(self,item):
		if(item.text() in self.canshu_new):
			item.setForeground(QColor(0,0,0))
			self.canshu_new.remove(item.text())
		else:
			item.setForeground(QColor(255,0,0))
			self.canshu_new.add(item.text())
		return
	
	def method_fun(self,btn):
		self.method = btn.text()
		return

	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
		return
if __name__ == "__main__":
	app = QApplication(sys.argv)
	fileload =	filedialogdemo()
	fileload.show()
	'''
	high,low,dopen,close,vol=get_data_fromDB('stock_900957')
	print(high)
	print('*******************')
	print(low)
	print('*******************')
	print(dopen)
	print('*******************')
	print(close)
	print('*******************')
	print(vol)
	print('*******************')
	'''
	sys.exit(app.exec_())
