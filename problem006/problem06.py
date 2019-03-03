# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:46:36 2019

@author: bronz0
"""

def sumOfSquares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i)
    return sum

def squareOfSum(n):
    sum = n*(n+1)/2 # = 1+2+3+...+n
    return sum*sum

def diff(n):
    return squareOfSum(n) - sumOfSquares(n)

# diff(100)
# the answer is 25164150