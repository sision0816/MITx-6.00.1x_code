# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:06:42 2016

@author: WenChen
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    md_num = ''
    if us_num in trans:
        md_num += trans[us_num]
    elif us_num [0] == '1':
        md_num += 'shi '+ trans[us_num[1]]
    elif us_num [1] == '0':
        md_num += trans[us_num[0]] +' shi'
    else:
        md_num += trans[us_num[0]] +' shi ' + trans[us_num[1]]
    return print (md_num)