#!/bin/python3

import os
import sys

#
# Complete the arraySplitting function below.
#
def arraySplitting(arr):
    #
    # Write your code here.
    #
    def split(su,arr):
        if su & 1 == 1:  # 奇数
            return 0
        target = su // 2
        #print(target,arr)
        s = 0
        n = len(arr)
        for i in range(n):
            s += arr[i]
            #print(i,s,target)
            if s == target:
                if i < n - 1:
                    return 1 + max(split(target,arr[:i + 1]),split(target,arr[i + 1:]))
                else:
                    return 0
            if s > target:
                break
        return 0
    
    su = sum(arr)
    if su == 0:
        return len(arr) - 1
    return split(su,arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
