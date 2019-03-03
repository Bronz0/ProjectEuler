# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:10:44 2019

@author: bronz0
"""
import numpy as np

def isFactor(n,x):
    quotion = n/x
    remainder = quotion - np.round(quotion)
    if(remainder == 0):
        return True
    else:
        return False
    
def devisible(n):
    # if n is devisible by 20 its also devisible by 10,5,2
    # if n is devisible by 18 its also devisible by 9,6,3,2
    # and so on, so no need to check if n is devisible by {1,2,3,4,5,6,7,8,9,10}
    for i in range(11,21):
       if(isFactor(n,i) == False):
           return False
    return True

def smallestMultiple():
    for i in range(2000000,1000000000,20):
        print(i)
        if(devisible(i)):
            return i
        
#smallestMultiple()
# the answer is 232792560