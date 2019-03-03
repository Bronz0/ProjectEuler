# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:12:57 2019

@author: bronz0
"""

import numpy as np

def divisorsNumber(n):
    cpt = 0;
    for i in range(1,int(np.sqrt(n)+1)):
        if(n%i == 0):
            cpt+=1
            if(n//i > i):
                cpt+=1
    return cpt 

notfound = True
n = 0
triangleNum = 0
while(notfound):
    n+=1
    triangleNum += n
    divNum = divisorsNumber(triangleNum)
    if(divNum > 500):
        notfound = False
    
print(triangleNum)
