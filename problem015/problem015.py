# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:15:03 2019

@author: pc
"""


from numpy import math
# in a n*n grid to move from the top left corner to the bottom right corner we need to performe exactly
# n moves right and n moves down in some order, Because each individual down or right move
# is indistinguishable, there are exactly 2N choose N (binomial coefficient) ways of arranging these moves.
print(math.factorial(40)/(math.factorial(20) * math.factorial(40-20)))

# Answer: 137846528820