# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:27:50 2019

@author: pc
"""

def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

s = 0
f = 1
i = 1

while(f<4000000):
    f = fibo(i)
    if(f%2 == 0):
        s += f
    i += 1 
    
print(s)