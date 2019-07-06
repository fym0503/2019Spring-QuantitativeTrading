import pymysql

tablename='stock_300354'


db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
cursor = db.cursor()
sql_high="""select high from """+tablename+r';'
#print(sql_high)
a=cursor.execute(sql_high)
high=cursor.fetchall()
print(type(high))
print(high)
'''
	sql_low="""select low from """+tablename+""";"""
	low=cursor.execute(sql_low)
	sql_dopen="""select open_ from """+tablename+""";"""
	dopen=cursor.execute(sql_dopen)
	sql_close="""select close from """+tablename+""";"""
	close=cursor.execute(sql_close)
	sql_vol="""select volume from """+tablename+""";"""
	vol=cursor.execute(sql_vol)
	return high,low,dopen,close,vol
'''

