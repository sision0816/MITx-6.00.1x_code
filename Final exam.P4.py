# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:06:42 2016

@author: WenChen
"""
def getSublists(L,n):
    outL=[]
    for i in range(0,len(L)-n+1):
        outL.append(L[i:i+n])
    return outL
def longest_run(L):
    for n in range(len(L), 0, -1):
        temp=getSublists(L,n)
        for subL in temp:
            if subL==sorted(subL) or subL==sorted(subL, reverse = True):
               return sum(subL)