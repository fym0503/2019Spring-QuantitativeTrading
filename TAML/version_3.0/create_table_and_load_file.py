import pymysql


i=['300354','300362','300371','300431','300462','300536','300588','300631']
db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
cursor = db.cursor()

for d in i:
    sql_del="""drop table stock_"""+d+";"
    print(sql_del)
    cursor.execute(sql_del)
    db.commit

for d in i:

    sql_cap = """create table stock_"""+d+"""(
date CHAR(25),
open_ DOUBLE,
high DOUBLE,
close DOUBLE,
low DOUBLE,
volume DOUBLE,
price_change DOUBLE,
p_change DOUBLE,
ma5 DOUBLE,
ma10 DOUBLE,
ma20 DOUBLE,
v_ma5 DOUBLE,
v_ma10 DOUBLE,
v_ma20 DOUBLE
);"""
    cursor.execute(sql_cap)
    db.commit()
print('*********************CRERATE FINISH**************************')
for d in i:
    sql="""load data infile 'E:/"""+d+""".csv'
into table stock_"""+d+r"""
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
IGNORE 1 ROWS;"""
    print(sql)
    cursor.execute(sql)
    db.commit()
