#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:18:04 2019

@author: faheem
"""

def fibo(n):
    if(n==2 or n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(10))