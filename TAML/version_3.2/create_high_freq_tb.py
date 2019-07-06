import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
cursor = db.cursor()
stock_name=['000004','000005','000006','000007','000008','000009','000011']

for d in stock_name:
    sql_del="""drop table if exists highfreq_stock_"""+d+";"
    #print(sql_del)
    cursor.execute(sql_del)
    db.commit()
for d in stock_name:
    sql_c = """create table highfreq_stock_"""+d+"""(
ID INT,
ts_code CHAR(25),
trade_time CHAR(25),
open_ DOUBLE,
high DOUBLE,
low DOUBLE,
close DOUBLE,
volume DOUBLE,
amount DOUBLE,
trade_date CHAR(25),
pre_close DOUBLE
);"""
    #print(sql_c)
    cursor.execute(sql_c)
    db.commit()

for d in stock_name:
    sql="""load data infile 'E:/Highfreq/"""+d+""".csv'
into table highfreq_stock_"""+d+r"""
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
IGNORE 1 ROWS;"""
    #print(sql_del)
    cursor.execute(sql)
    db.commit()