#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:12:59 2019

@author: faheem
"""
dsp=[]
for l in range(200):
    count=0
    num=l
    for i in range(2,num):
        if(num%i==0):
            count+=1
        else:
            continue
        k=0
        while(num%i==0):
            num/=i
            k+=1
    if(count==2 and k<2):
        dsp.append(l)
    else:
        continue
print(dsp)
m=0
n=int(input())
for ele in dsp:
    s=n-ele
    for ele in dsp:
        if(ele==s):
            m=1
            break
        else:
            continue
if(m==1):
    print("Yes")
else:
    print("No")