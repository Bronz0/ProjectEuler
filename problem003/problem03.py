# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:33:44 2019

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


def isFactor(n,x):
    quotion = n/x
    fraction = quotion - np.round(quotion)
    if(fraction == 0):
        return True
    else:
        return False
    
    
def lagestPrimeFactor(n):
    x = np.round(0.5+np.sqrt(n))
    i = x
    while(i>=2):
        if(isPrime(i)):
            if(isFactor(n,i)):
                return i
        i = i-1;
        
n = 600851475143
# lagestPrimeFactor(n)
# the answer is 6857