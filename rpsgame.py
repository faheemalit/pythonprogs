#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:24:37 2019

@author: faheem
"""
x1=input("p1")
x2=input("p2")
pt1=0
pt2=0
list(x1)
list(x2)
for i in range(len(x1)):
    if(x1[i]==x2[i]):
        continue
    elif((x1[i]=="0" and x2[i]=="2") or (x1[i]=="1" and x2[i]=="0") or (x1[i]=="2" and x2[i]=="1")):
        pt1+=1
    else:
        pt2+=1
print(pt1)
print(pt2)  
        #p1 wins