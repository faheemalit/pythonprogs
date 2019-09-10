#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:03:27 2019

@author: faheem
"""

# Python program showing 
# Graphical representation of 
# exp() function 
import numpy as np 
import matplotlib.pyplot as plt 

in_array = [1, 1.2, 1.4, 1.6, 1.8, 2] 
out_array = np.exp(in_array) 

y = [1, 1.2, 1.4, 1.6, 1.8, 2] 
plt.plot(in_array, y, color = 'blue', marker = "*") 

# red for numpy.exp() 
plt.plot(out_array, y, color = 'red', marker = "o") 
plt.title("numpy.exp()") 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.show() 
