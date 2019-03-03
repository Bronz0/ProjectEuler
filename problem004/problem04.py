# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:22:52 2019

@author: bronz0
"""

def isPalindrome(n):
    realNumber = n
    reversedNumber = 0
    while(n != 0):
        remainder = n%10
        reversedNumber = reversedNumber*10 + remainder
        n = (n-remainder)/10
    if(realNumber == reversedNumber):
        return True
    else:
        return False
    
def largestPalindrome():
    i = 999
    largest = 0
    while(i>100):
        j = i-1
        while(j>99):
            x = i*j
            if(isPalindrome(x)):
                if(x>largest):
                    largest = x
            j = j-1
        i = i-1
        print(i)
    return largest
        

# largestPalindrome()
# the answer is 906609