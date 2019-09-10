#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:42:59 2019

@author: faheem
"""
import numpy
print("Magic Square")
n=int(input("Enter the Order of Magic Square: "))
magicsq=numpy.zeros((n,n))
num=n*n
i=int(n/2)
j=n-1
for k in range(1,num+1):
    if(magicsq[i][j]!=0):
        i=(i+1)%n
        j=(j-2)%n
    elif(i==-1 and j==0):
        i=0
        j=n-2
    magicsq[i][j]=k
    i=((i-1)+n)%n
    j=((j+1)+n)%n
print(magicsq)