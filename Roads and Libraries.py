#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    cityLeft = n
    #roadNeeded = 0
    if c_lib <= c_road:
        return n * c_lib
    cityGroup = {}
    cityRoads = {}
    for ca,cb in cities:
        if ca in cityRoads:
            cityRoads[ca].add(cb)
        else:
            cityRoads[ca] = {cb}
        if cb in cityRoads:
            cityRoads[cb].add(ca)
        else:
            cityRoads[cb] = {ca}
        cityGroup[ca] = True
        cityGroup[cb] = True
    #print(cityRoads)
    #print(cityGroup)
    toGroup = set()
    for e in cityGroup:
        # cityGroup[i] >= i
        #print(e,cityGroup,cityRoads)
        if e in cityRoads:
            toGroup |= cityRoads[e]
            while toGroup:
                #print(e,toGroup)
                c = toGroup.pop()
                #print(c)
                if c in cityGroup and cityGroup[c] and c != e:
                    cityGroup[c] = False
                    cityLeft -= 1
                    #roadNeeded += 1
                if c in cityRoads:
                    #print(toGroup)
                    toGroup |= cityRoads[c]
                    #print(toGroup,cityRoads[c])
                    del cityRoads[c]
                #print(e,c,toGroup,cityGroup,cityRoads)
    print(cityGroup)
    #cityLeft = len(cityGroup)
    #print(cityLeft,roadNeeded)
    return c_lib * cityLeft + c_road * (n - cityLeft)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
