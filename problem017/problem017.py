# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:02:00 2019

@author: bronz0
"""

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def to_letters(n):
    if(0 < n <= 19):
        return ones[n]
    elif(20 <= n <= 99):
        return tens[n//10] + ones[n%10]
    elif(100 <= n <= 999):
        return ones[n//100] + "hundred" + (("and" + to_letters(n % 100)) if (n % 100 != 0) else "")
    elif n==1000:
        return "onethousand"

def count():
    cpt = 0
    for i in range(1,1001):
        cpt += len(to_letters(i))
    print(cpt)

count()
        
# the answer : 21124