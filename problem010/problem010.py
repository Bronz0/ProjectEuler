# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:21:54 2019

@author: bronz0
"""
import numpy as np
def isPrime(n):
    if(n<4):
        return True;
    else:
        a = np.sqrt(n)
        i = 2
        while (i<=a):
            if(n%i == 0):
                return False
            i = i+1
        return True
s = 0;
for i in range(2,2000001):
     if(isPrime(i)):
         s += i

print(s)