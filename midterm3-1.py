# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:13:16 2016

@author: WenChen
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x