# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:32:21 2016

@author: WenChen
"""

balance = 3329
annualInterestRate = 0.2
lowestPayment = 10
def debt (n):
    unpaied = balance - lowestPayment
    balance1 = unpaied *(1+annualInterestRate/12)
    if n == 1:
        return balance1
    else:
        return (debt(n-1)-lowestPayment)*(1+annualInterestRate/12)
while debt(12)>0:
      lowestPayment = 10 + lowestPayment
      print (debt(12))
print (lowestPayment)
 