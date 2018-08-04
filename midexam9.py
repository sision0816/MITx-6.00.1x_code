# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 23:34:47 2016

@author: WenChen
"""

''' 
aList: a list 
Returns a copy of aList, which is a flattened version of aList 
'''
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
