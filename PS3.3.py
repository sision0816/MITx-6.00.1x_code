# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:42:13 2016

@author: WenChen
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    returnWord = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            returnWord += i
    return returnWord