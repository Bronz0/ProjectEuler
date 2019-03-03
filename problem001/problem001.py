# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:22:46 2019

@author: pc
"""
result = 0
for i in range(3,1000):
    if(i%3 == 0 or i%5==0):
        result += i
    
print(result)

# the answer is 233168