nameall=[]
import pymysql
'''

trynamenum=300000

for i in range(601000):
    tryname=str(trynamenum)
    try:
        f =open('E:/stock_data/'+tryname+'.csv')
        nameall.append(tryname)
        f.close()
        trynamenum+=1
    except IOError:
        trynamenum+=1
    #print "File is not accessible."
print(nameall)

#print(name)
name=nameall

db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
cursor = db.cursor()

for d in name:
    sql_del="""drop table if exists stock_"""+d+";"
    print(sql_del)
    cursor.execute(sql_del)
    db.commit

for d in name:

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
'''
for d in name:
    sql="""load data infile 'E:/stock_data/"""+d+""".csv'
into table stock_"""+d+r"""
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
IGNORE 1 ROWS;"""
    print(sql)
    cursor.execute(sql)
    db.commit()

'''

namewith0=[]

trynamewith0='00000'
b=1
nametest=trynamewith0+str(b)
#print(nametest)

for i in range(10):
    tryname=trynamewith0+str(b)
    try:
        f =open('E:/stock_data/'+tryname+'.csv')
        namewith0.append(tryname)
        f.close()
        b+=1
    except IOError:
        
        b+=1
#print(namewith0)

c=10
trynamewith0='0000'
for i in range(100):
    tryname=trynamewith0+str(c)
    try:
        f =open('E:/stock_data/'+tryname+'.csv')
        namewith0.append(tryname)
        f.close()
        c+=1
    except IOError:
        
        c+=1
#print(namewith0)

d=100
trynamewith0='000'
for i in range(1000):
    tryname=trynamewith0+str(d)
    try:
        f =open('E:/stock_data/'+tryname+'.csv')
        namewith0.append(tryname)
        f.close()
        d+=1
    except IOError:
        
        d+=1
#print(namewith0)

d=1000
trynamewith0='00'
for i in range(10000):
    tryname=trynamewith0+str(d)
    try:
        f =open('E:/stock_data/'+tryname+'.csv')
        namewith0.append(tryname)
        f.close()
        d+=1
    except IOError:
        
        d+=1
print(namewith0)


'''

db = pymysql.connect(host='127.0.0.1', user='root', passwd='ZXY2001zxy*', db='stock', charset='utf8')
cursor = db.cursor()

for d in namewith0:
    sql_del="""drop table if exists stock_"""+d+";"
    print(sql_del)
    cursor.execute(sql_del)
    db.commit

for d in namewith0:

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
#print('*********************CRERATE FINISH**************************')
for d in namewith0:
    sql="""load data infile 'E:/stock_data/"""+d+""".csv'
into table stock_"""+d+r"""
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
IGNORE 1 ROWS;"""
    #print(sql)
    cursor.execute(sql)
    db.commit()

