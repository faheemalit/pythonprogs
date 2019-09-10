#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:39:18 2019

@author: faheem
"""
import random
doors=[0,0,0]
goatdoor=[]
j=0
swap=0
dontswap=0
for j in range(10000):
    x=random.randint(0,2)
    for i in range(3):
        if(i==x):
            doors[i]="BMW"
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=random.randint(0,2)
    if(j%2==0):
        if(doors[choice]=="BMW"):
            dontswap+=1
        else:
            continue
    else:
        if(doors[choice]=="BMW"):
            continue
        else:
            swap+=1            
print(swap)
print(dontswap)