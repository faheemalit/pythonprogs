#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:29:02 2019

@author: faheem
"""
r,c=input().split()
r=int(r)
c=int(c)
matrix=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append(0)
    matrix.append(l)
n=1
while(n<r*c+1):
    for i in range(0,r):
        for j in range(0,c):
            matrix[i][j]=n
            n+=1
for i in range(0,r):    
    for j in range(0,c-1):
        print(matrix[i][j],end=" ")
    j+=1
    if(i<r-1):
        print(matrix[i][j])
    else:
        print(matrix[i][j],end="")
    