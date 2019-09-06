#!/bin/python

import sys

import math
def lowestTriangle(base, area):
    # Complete this function
    return int(math.ceil(area * 2.0 / base))

base, area = raw_input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)

