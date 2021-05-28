#!/usr/bin/env python
# coding: utf-8

import pytz, datetime  ##importing libraries
year = int(input())
month = int(input())
day = int(input())
hours = int(input())
minutes= int(input())

#converting into timestamp
curr_date=datetime.datetime(year,month,day,hours,minutes) #converting into timestamp

#To get time of that city
cairo_tz=pytz.timezone('Africa/cairo') #To get time of that city
london_tz=pytz.timezone('utc')
Newdelhi_tz=pytz.timezone('Asia/kolkata')
Sydney_tz=pytz.timezone('Australia/sydney') 


cairo_time=pytz.utc.localize(curr_date).astimezone(cairo_tz) 
london_time=pytz.utc.localize(curr_date).astimezone(london_tz)
Newdelhi_time=pytz.utc.localize(curr_date).astimezone(Newdelhi_tz)
Sydney_time=pytz.utc.localize(curr_date).astimezone(Sydney_tz)

#print Timestamp of particular city in ISO format

print("Cairo Time is",cairo_time.isoformat())  
print("London Time is",london_time.isoformat())
print("New Delhi Time is",Newdelhi_time.isoformat())
print("Sydney Time is",Sydney_time.isoformat())




