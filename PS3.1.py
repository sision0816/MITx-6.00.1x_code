# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:49:03 2016

@author: WenChen
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in range(len(secretWord)):
#        print (secretWord[i])
        if secretWord[i] not in lettersGuessed:
            return False
            break
    return True
            
             
