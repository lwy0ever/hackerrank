#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    ans = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.match(r'[a-z.]+@gmail.com',emailID):
            ans.append(firstName)
    ans.sort()
    [print(e) for e in ans]

