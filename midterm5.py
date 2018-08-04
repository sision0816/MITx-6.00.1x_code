# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:04:56 2016

@author: WenChen
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    i = 0 
    product = 0
    for i in range(len(listA)):
        product += listA[i] * listB[i]
    return product