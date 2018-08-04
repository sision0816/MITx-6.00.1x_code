# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:26:29 2016

@author: WenChen
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    returnWord = ''
    for i in range(len(secretWord)):
#       print (secretWord[i])
        if secretWord[i] in lettersGuessed:
            returnWord += secretWord[i]
        else:
            returnWord += '_ '
    return returnWord