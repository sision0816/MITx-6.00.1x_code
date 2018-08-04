# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:45:08 2016

@author: WenChen
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    guess = 0
    exponent = 0
    if num >= 1:
       while base**guess < num:
           guess+=1
       if abs(base**guess - num) < abs (base**(guess -1) - num):
           exponent = guess
       else:
           exponent = guess - 1
    else:
        while base**guess > num:
            guess-=1
        if abs(base**guess - num) < abs (base**(guess -1) - num):
           exponent = guess
        else:
           exponent = guess - 1
    return exponent