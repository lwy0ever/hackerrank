#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = bin(n)
    print(max([len(v) for v in re.findall('1+',b)]))

