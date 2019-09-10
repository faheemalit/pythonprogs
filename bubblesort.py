#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:33:28 2019

@author: faheem
"""

a=[8,22,7,9,31,5,13]
k=6
swap=0
for i in range(6):
    for j in range(k):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            swap+=1
        else:
            continue
    k-=1
print(a)
print(swap)