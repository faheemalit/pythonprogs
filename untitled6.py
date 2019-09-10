#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:18:04 2019

@author: faheem
"""

import math 
for l in range(2,200):
    num=l
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1): 
		while num % i == 0: 
			num /= i 
			cnt += 1 
		if cnt >= 2: 
			break
	if(num > 1): 
		cnt += 1
	return cnt == 2