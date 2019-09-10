#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:30:35 2019

@author: faheem
"""
a=list(map(int,input().split()))
n=len(a)
b=[]
for i in range(len(a)):
    b.append(a[i])
b.sort()
print(a)
print(b)
for i in range(len(a)):
    if(a[i]==b[i]):
        n-=1
    else:
        continue
print(n)