#!/usr/bin/env python3

import pymysql


conn = pymysql.connect(host='192.168.8.208', port=3306, user='liangyj', passwd='566560.com', db='mytest')

cursor = conn.cursor()

effect_row = cursor.execute("select * from score")

# print(cursor.fetchone())
print(cursor.fetchall())

conn.commit()

cursor.close()

conn.close()