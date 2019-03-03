# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:49:23 2019

@author: pc
"""


def collatz(n):
    cpt = 1
    while(n>1):
        if(n%2 == 0):
            n = n/2
        else:
            n = n*3 + 1
        cpt +=1
    return cpt

maximum = 0
n = 0
for i in range(1000000):
    c = collatz(i)
    if(maximum < c):
        maximum = c
        n = i
print(n)

# the answer is 837799"""""""""""""""""""
    
    