#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:59:18 2019

@author: faheem
"""
import random
n=int(input("number of elements"))
i=1
a=[]
for k in range(n):
    temp=int(input())
    a.append(temp)
acopy=a
b=[]
for l in acopy:
    b.append(l)
print(b)
for s in range(n):
    l=random.choice(a)
    a.remove(l)
    b[s]=l
print(b)
print(a)