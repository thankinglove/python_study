#! /usr/bin/env python

import datetime

# help(datetime)

now_time = datetime.datetime.now()
print("datetime.datetime.now(): ", now_time)
date = now_time.date()
print("date: ", date)

three_days_ago = now_time + datetime.timedelta(days=-3)
print("three_days_agp: ", three_days_ago)