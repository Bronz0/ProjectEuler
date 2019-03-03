# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:16:23 2019

@author: bronz0
"""

import numpy as np

for a in range(1,1000):
    for b in range(1,1000):
        c = np.sqrt(a*a + b*b)
        if((a + b + c)==1000):
            print(a, b, c)
            print("produit = ", a*b*c)
            