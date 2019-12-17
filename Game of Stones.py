#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfStones function below.
def gameOfStones(n):
    ans = [0] # ans[i]=0表示i个stone时，先走会输，1表示先走会赢
    for i in range(1,n + 1):
        # 尝试取2,3,5中的一个,使对方输
        if i - 2 >= 0 and ans[i - 2] == 0 or i - 3 >= 0 and ans[i - 3] == 0 or i - 5 >= 0 and ans[i - 5] == 0:
            ans.append(1)
        else:
            ans.append(0)
    #print(ans)
    return 'First' if ans[-1] else 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
