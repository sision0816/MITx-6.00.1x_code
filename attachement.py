# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# define a function of polysum
def polysum (n,s):
# the variable is n and s
# n is the number of sides
# s is the length of each side
    import math
#import math module, in order to apply the tan function and pi
    area = 0.25*n*s**2/math.tan(math.pi/n)
# calculcation of area
    perimeter = n*s
# calculation of length of the regular polygum
    sum = area + perimeter**2
    return round (sum, 4)
# apply the build-in round function to round the 4 decimal places.