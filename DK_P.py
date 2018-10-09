# -*- coding: UTF-8 -*-

import datetime
dt = datetime.datetime.now()
t1 = dt.timestamp()

import random
m1 = random.randint(60,600)
tp = t1+m1
t3 = datetime.datetime.fromtimestamp(tp)
time = t3.strftime("%Y-%m-%d %H:%M:%S")

import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.2.11;DATABASE=ms3000II;UID=sa;PWD=txtv-1234')
cursor = cnxn.cursor()

P = "insert into u_kqRecord (sbID,gZT,gTime,uID) values ('G1',0,'"+time+"','1148')"

C = "select count(*) from u_kqRecord where DateDiff(dd,gTime,getdate())=0"

cursor.execute(C)
data = cursor.fetchone()
d1 = str(data)

import re

d2=(re.findall(r"\d+",d1))
d3=int(''.join(map(str, d2)))

if d3 > 80:
    cursor.execute(P)
    cnxn.commit()
    cnxn.close()
else:
    cnxn.close()