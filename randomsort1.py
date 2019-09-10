#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:44:01 2019

@author: faheem
"""

import random
n=int(input("number of elements"))
i=1
a=[]
index=[]
for k in range(n):
    temp=int(input())
    a.append(temp)
print(a)
sortd=0
t=0
while(sortd==0):
    u=0
    t+=1
    i=random.randint(0,n-1)
    j=random.randint(0,n-1)
    m=a[i]
    a[i]=a[j]
    a[j]=m
    s=0
    while(s<n-1):
        if(a[s]>a[s+1]):
            break
        else:
            u+=1
        s+=1
    if(u==n-1):
        sortd=1
print(a)
for j in range(0,n):
    if(j<n-1):
        print(a[j],end=" ")
    else:
        print(a[j],end="")