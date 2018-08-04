# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 15:05:58 2016

@author: WenChen
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for element in L:
        element.reverse()
    