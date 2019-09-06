#!/bin/python3

import math
import os
import random
import re
import sys

import copy
# Complete the crosswordPuzzle function below.
def findPos(cross,word):
    ans = []
    l = len(word)
    for i in range(10):
        for j in range(10 - l + 1):
            for c in range(l):
                #print(i,j,c,word)
                #print(cross[i])
                if cross[i][j + c] not in ('-',word[c]):
                    break
            else:
                #print('in findPos',word)
                #print('\n'.join(cross))
                #print(i,j,'x')
                ans.append((i,j,'x'))
    for i in range(10 - l + 1):
        for j in range(10):
            for c in range(l):
                if cross[i + c][j] not in ('-',word[c]):
                    break
            else:
                #print('in findPos',word)
                #print('\n'.join(cross))
                #print(i,j,'y')
                ans.append((i,j,'y'))
    return ans

def fill(cross,word,pos):
    if pos[2] == 'x':
        #print(cross[pos[0]])
        cross[pos[0]] = cross[pos[0]][:pos[1]] + word + cross[pos[0]][pos[1] + len(word):]
        #print(cross[pos[0]])
    else:
        for i in range(len(word)):
            cross[pos[0] + i] = cross[pos[0] + i][:pos[1]] + word[i] + cross[pos[0] + i][pos[1] + 1:]

def crosswordPuzzle(crossword, words):
    if len(words) == 0:
        return crossword
    #print('words:',words)
    word = words.pop()
    #print('\n'.join(crossword))
    for pos in findPos(crossword,word):
        #print('try:',word,pos)
        oldCross = copy.deepcopy(crossword)
        fill(crossword,word,pos)
        #print('\n'.join(crossword))
        result = crosswordPuzzle(crossword,words)
        if result:
            return result
        crossword = oldCross
        #print('revert')
        #print('\n'.join(crossword))
    words.append(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()
    words = words.split(';')

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
