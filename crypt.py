#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 07:05:17 2019

@author: faheem
"""

import string
dict ={}
for i in range(len(string.ascii_letters)+1):
    dict[string.ascii_letters[i]]=string.ascii_letters[i+1]
print(dict)