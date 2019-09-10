#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:10:51 2019

@author: faheem
"""
import datetime
import random
i=0
doy=[]
while(i<50):
    year=random.randint(1880,2018)
    if(year%400==0):
        leapyear=1
    elif(year%100!=0 and year%4==0):
        leapyear=1
    else:
        leapyear=0
    month=random.randint(1,12)
    if(month==2):
        if(leapyear):
            days=29
        else:
            days=28
    elif(month<8):
        if(month%2==1):
            days=31
        else:
            days=30
    else:
        if(month%2==0):
            days=31
        else:
            days=30
    day=random.randint(1,days)
    dob=datetime.date(year,month,day)
    i+=1
    dy=dob.timetuple().tm_yday
    doy.append(dy)
doy.sort()
print(doy)