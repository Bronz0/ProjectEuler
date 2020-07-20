# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:15:47 2019

@author: bronz0
"""

def digitSum(n):
    s = 0
    while(n>0):
        s += n%10
        n = n//10
    return s

print(digitSum(2**1000))

# Answer: 1366

# method 2 
print(sum([int(x) for x in str(2**1000)]))