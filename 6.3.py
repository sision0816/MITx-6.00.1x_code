# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:05:50 2016

@author: WenChen
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    dictValues = aDict.values()
    valuesList = []
    for valuesElement in dictValues:
        valuesList += valuesElement
    return len(valuesList)