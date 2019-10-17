#!/bin/python3

import math
import os
import random
import re
import sys

def Hanoi(a):
    visited = {''.join(map(str,a))}
    target = '1' * N
    fromStat = {''.join(map(str,a))}
    ans = 0
    while True:
        if target in fromStat:
            return ans
        toStat = set()
        for st in fromStat:
            # 尝试将disc i移动到每个rob上
            # cantRob 记录比i小的disc存在的rob,这些rob是不能放置disc i的
            cantRob = set()
            for i in range(N):
                # 可能的目标rob
                #move_target = {str(x) for x in range(1,5)}
                move_target = {'1','2','3','4'}
                if st[i] in cantRob:
                    continue
                cantRob.add(st[i])
                move_target = move_target.difference(cantRob)
                if not move_target:
                    break
                for t in move_target:
                    new_stat = st[:i] + t + st[i + 1:]
                    #print('%s->%s,%s'%(st,new_stat,move_target))
                    if new_stat not in visited:
                        toStat.add(new_stat)
                        visited.add(new_stat)
        fromStat = toStat
        ans += 1
        #print(ans,fromStat)
        #print(visited)

if __name__ == '__main__':
    N = int(input())

    a = list(map(int, input().rstrip().split()))

    print(Hanoi(a))
