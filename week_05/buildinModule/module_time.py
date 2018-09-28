#! /usr/bin/env python

# import sys
# import os
import time

now_time = time.time()
print("time.time: ", now_time)

x = time.gmtime(now_time)
print("time.gmtime: ", x)

print("x.tm_year: ", x.tm_year)
print("x.tm_mon: ", x.tm_mon)
print("x.tm_mday: ", x.tm_mday)
print("x.tm_hour: ", x.tm_hour)
print("x.tm_min: ", x.tm_min)
print("x.tm_sec: ", x.tm_sec)
print("x.tm_wday: ", x.tm_wday)


print(x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min,  x.tm_sec, x.tm_wday, x.tm_yday, x.tm_isdst,
      x.tm_zone, x.tm_gmtoff)

y = time.mktime(x)
print("time.mktime: ", y)

z = time.strftime("%Y-%m-%d %H:%M:%S", x)
print("time.strftime: ", z)

d = time.strptime(z, "%Y-%m-%d %H:%M:%S")
print("time.strptime: ", d)

t1 = time.asctime()
print("time.asctime(): ", t1)

t2 = time.asctime(x)
print("time.asctime(tuple): ", t2)

m1 = time.ctime(time.time())
print("time.ctime(time.time()): ", m1)

m2 = time.ctime()
print("time.ctime(): ", m2)