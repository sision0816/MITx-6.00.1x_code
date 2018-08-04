# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:26:54 2016

@author: WenChen
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code 
    valueNumber = []
    dictKeys = list (aDict.keys())
    for dictValues in aDict.values():
        length = len(dictValues)
        valueNumber.append(length)
        print (length)
    for i in range(len(valueNumber)):
        if valueNumber[i] == max (valueNumber):
            return dictKeys[i] 