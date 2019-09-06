#!/bin/python3

# unfinished version

import math
import os
import random
import re
import sys

def change():
    s = [[['',''] for _ in range(width)] for _ in range(width)]
    #print(s)
    for x in white:
        s[int(x[2]) - 1][ord(x[1]) - ord('A')][0] = x[0]
        s[int(x[2]) - 1][ord(x[1]) - ord('A')][1] = 'w'
    for x in black:
        s[int(x[2]) - 1][ord(x[1]) - ord('A')][0] = x[0]
        s[int(x[2]) - 1][ord(x[1]) - ord('A')][1] = 'b'
    #print(s)
    #show(s)
    return s

def copy(chess):
    s = [[['',''] for _ in range(width)] for _ in range(width)]
    for r in range(len(chess)):
        for c in range(len(chess[r])):
            s[r][c][0] = chess[r][c][0]
            s[r][c][1] = chess[r][c][1]
    return s

def show(chess):
    return
    for r in range(len(chess) - 1,-1,-1):
        print('%d:' %(r + 1), end = '')
        for c in range(len(chess[r])):
            if chess[r][c][1] == 'b':
                print('\033[32m' + chess[r][c][0] + '\033[0m',end = '\t')
            else:
                print(chess[r][c][0],end = '\t')
        print()
    print('*:1\t2\t3\t4\t')
    #input('--1\t2\t3\t4\t')

def whomove(who,chess,stepLeft):
    #os.system('cls')
    if who == 'w' and stepLeft <= 0 or who == 'b' and stepLeft <= 1:
        #print('No step left')
        return False
    for r in range(len(chess)):
        #逐个棋子尝试
        for c in range(len(chess[r])):
            p = chess[r][c]
            #print(chess,r,c)
            #print(p[1],who,p[1] != who)
            if p[1] != who:
                continue
            #print('!!!')
            if p[0] != 'P':
                #逐个方向尝试
                for d in rule[p[0]]['both']:
                    #逐个距离尝试
                    #print(rule,p[0],who)
                    for s in range(1,rule[p[0]]['step'] + 1):
                        #检查越界
                        if c + d[0] * s < 0 or c + d[0] * s >= width or r + d[1] * s < 0 or r + d[1] * s >= width:
                            break
                        tryMove = move(chess,r,c,d[1] * s,d[0] * s)
                        if tryMove[0]:
                            #移动并攻击
                            newChess = copy(chess)
                            newChess[r + d[1] * s][c + d[0] * s][0] = newChess[r][c][0]
                            newChess[r + d[1] * s][c + d[0] * s][1] = newChess[r][c][1]
                            newChess[r][c][0] = ''
                            newChess[r][c][1] = ''
                            #print('color   %s : step   %d' % (who,m - stepLeft + 1))
                            show(chess)
                            #print('%s @ %d,%d move %d,%d' % (p,r + 1,c + 1,d[1] * s,d[0] * s))
                            show(newChess)
                            if whoWin(newChess) == 'w':
                                print('YES')
                                #input()
                                exit()
                                break
                            elif whoWin(newChess) == 'b':
                                #print('black win')
                                break
                            #input()
                            if who == 'w':
                                whomove('b',newChess,stepLeft)
                            else:
                                whomove('w',newChess,stepLeft - 1)
                        if not tryMove[1]:
                            #此方向移动失败，不进行更长距离尝试
                            break
            else:    # p[0] == P
                #逐个方向尝试
                #只移动，不攻击
                for d in rule[p[0]][who]['move']:
                    #逐个距离尝试
                    for s in range(1,rule[p[0]]['step'] + 1):
                        #检查越界
                        if c + d[0] * s < 0 or c + d[0] * s >= width or r + d[1] * s < 0 or r + d[1] * s >= width:
                            break
                        tryMove = move(chess,r,c,d[1] * s,d[0] * s)
                        if tryMove[0] and tryMove[1]:
                            newChess = copy(chess)
                            newChess[r + d[1] * s][c + d[0] * s][0] = newChess[r][c][0]
                            newChess[r + d[1] * s][c + d[0] * s][1] = newChess[r][c][1]
                            newChess[r][c][0] = ''
                            newChess[r][c][1] = ''
                            #promote use newChess
                            if who == 'w' and r + d[1] * s == width - 1 or who == 'b' and r + d[1] * s == 0:
                                for newP in ['B','N','R']:
                                    newChess[r + d[1] * s][c + d[0] * s][0] = newP
                                    #print('color   %s : step   %d' % (who,m - stepLeft + 1))
                                    show(chess)
                                    #print('%s @ %d,%d move %d,%d' % (p,r + 1,c + 1,d[1] * s,d[0] * s))
                                    #show(newChess)
                                    #input()
                                    if who == 'w':
                                        whomove('b',newChess,stepLeft)
                                    else:
                                        whomove('w',newChess,stepLeft - 1)
                            else:
                                #print('color   %s : step   %d' % (who,m - stepLeft + 1))
                                show(chess)
                                #print('%s @ %d,%d move %d,%d' % (p,r + 1,c + 1,d[1] * s,d[0] * s))
                                show(newChess)
                                #input()
                                if who == 'w':
                                    whomove('b',newChess,stepLeft)
                                else:
                                    whomove('w',newChess,stepLeft - 1)
                        if not tryMove[1]:
                            #此方向移动失败，不进行更长距离尝试
                            break
                #攻击
                for d in rule[p[0]][who]['att']:
                    #逐个距离尝试
                    for s in range(1,rule[p[0]]['step'] + 1):
                        #检查越界
                        if c + d[0] * s < 0 or c + d[0] * s >= width or r + d[1] * s < 0 or r + d[1] * s >= width:
                            break
                        tryMove = move(chess,r,c,d[1] * s,d[0] * s)
                        if tryMove[0] and not tryMove[1]:
                            newChess = copy(chess)
                            newChess[r + d[1] * s][c + d[0] * s][0] = newChess[r][c][0]
                            newChess[r + d[1] * s][c + d[0] * s][1] = newChess[r][c][1]
                            newChess[r][c][0] = ''
                            newChess[r][c][1] = ''
                            #todo promote use copy
                            if who == 'w' and r + d[1] * s == width - 1 or who == 'b' and r + d[1] * s == 0:
                                for newP in ['B','N','R']:
                                    newChess[r + d[1] * s][c + d[0] * s][0] = newP
                                    #print('color   %s : step   %d' % (who,m - stepLeft + 1))
                                    show(chess)
                                    #print('%s @ %d,%d move %d,%d' % (p,r + 1,c + 1,d[1] * s,d[0] * s))
                                    show(newChess)
                                    if whoWin(newChess) == 'w':
                                        print('YES')
                                        #input()
                                        exit()
                                        break
                                    elif whoWin(newChess) == 'b':
                                        #print('black win')
                                        break
                                    #input()
                                    if who == 'w':
                                        whomove('b',newChess,stepLeft)
                                    else:
                                        whomove('w',newChess,stepLeft - 1)
                            else:
                                #print('color   %s : step   %d' % (who,m - stepLeft + 1))
                                show(chess)
                                #print('%s @ %d,%d move %d,%d' % (p,r + 1,c + 1,d[1] * s,d[0] * s))
                                show(newChess)
                                if whoWin(newChess) == 'w':
                                    print('YES')
                                    #input()
                                    exit()
                                    break
                                elif whoWin(newChess) == 'b':
                                    #print('black win')
                                    break
                                #input()
                                if who == 'w':
                                    whomove('b',newChess,stepLeft)
                                else:
                                    whomove('w',newChess,stepLeft - 1)
                        if not tryMove[1]:
                            #此方向移动失败，不进行更长距离尝试
                            break

def whoWin(chess):
    whiteWin = True
    blackWin = True
    for r in range(len(chess)):
        for c in range(len(chess[r])):
            if chess[r][c] == ['Q','b']:
                whiteWin = False
            if chess[r][c] == ['Q','w']:
                blackWin = False
    #print(whiteWin,blackWin)
    if whiteWin:
        return 'w'
    elif blackWin:
        return 'b'
    else:
        return 'none'

def move(chess,r,c,dr,dc):
    #第一个返回值表示是否可以移动
    #第二个返回值表示是否尝试更长距离
    if chess[r + dr][c + dc][1] == '':
        return True,True
    #新位置有同色棋子
    elif chess[r][c][1] == chess[r + dr][c + dc][1]:
        return False,False
    #异色棋子
    else:
        return True,False

def promote():
    pass

if __name__ == '__main__':
    g = int(input())    
    g = 1

    for _ in range(g):
        wbm = input().split()

        w = int(wbm[0])

        b = int(wbm[1])

        m = int(wbm[2])

        white = []

        for _ in range(w):
            white.append(input().rstrip().split())

        black = []

        for _ in range(b):
            black.append(input().rstrip().split())

        # Write Your Code Here
        width = 4
        os.system('')
        #print(white,black)
        originChess = change()
        #print(pieces)
        #print(pieces[:w])
        #print(pieces[-b:])
        rule = {
            'Q':{'both':[],'step':99},
            'N':{'both':[],'step':1},
            'B':{'both':[],'step':99},
            'R':{'both':[],'step':99},
            'P':{'step':1,'w':
                    {'move':[],
                    'att':[]},
                    'b':
                    {'move':[],
                    'att':[]}}}
        #后
        rule['Q']['both'] = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        #马
        rule['N']['both'] = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
        #象
        rule['B']['both'] = [[-1,-1],[-1,1],[1,-1],[1,1]]
        #车
        rule['R']['both'] = [[-1,0],[0,-1],[0,1],[1,0]]
        #兵
        rule['P']['w']['move'] = [[0,1]]
        rule['P']['w']['att'] = [[-1,1],[1,1]]
        rule['P']['b']['move'] = [[0,-1]]
        rule['P']['b']['att'] = [[-1,-1],[1,-1]]
        #print(rule)
        show(originChess)
        chess = copy(originChess)
        whomove('w',chess,m)
        show(originChess)
        print('NO')
