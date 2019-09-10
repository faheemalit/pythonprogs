#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:59:14 2019

@author: faheem
"""
import random
n=int(input("number of elements"))
i=1
a=[]
acopy=[]
for k in range(n):
    temp=int(input())
    a.append(temp)
for m in a:
    acopy.append(m)
b=[]
for l in a:
    b.append(l)
sortd=0
t=0
while(sortd==0):
    t+=1
    for l in acopy:
        a.append(l)
    i=0
    for s in range(n):
        l=random.choice(a)
        a.remove(l)
        b[s]=l
    acopy.sort()
    if(b==acopy):
        sortd=1
    else:
        sortd=0
print(acopy)
print(b)
print(t)
    
    