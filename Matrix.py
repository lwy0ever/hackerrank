#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(roads, machines):
    n = len(roads) + 1
    time_road = {}
    ma = set(machines)
    for r in roads:
        if r[2] in time_road:
            time_road[r[2]].append((r[0],r[1]))
        else:
            time_road[r[2]] = [(r[0],r[1])]
    #print(time_road)
    city_group = [i for i in range(n)]
    #print(city_group)
    city_connected = [[i] for i in range(n)]
    #print(city_connected)
    #print(city_group)
    totalConnected = 0
    totalDisconnected = 0
    for t in sorted(time_road.keys(),reverse = True):
        for r in time_road[t]:
            a = min(r[0],r[1])
            b = max(r[0],r[1])
            if city_group[a] in ma and city_group[b] in ma:
                totalDisconnected += t
                continue
            totalConnected += t
            if city_group[a] in ma:
                city_connected[a] += city_connected[b]
                for c in city_connected[a]:
                    city_group[c] = city_group[a]
                    city_connected[c] = city_connected[a]
            elif city_group[b] in ma:
                city_connected[b] += city_connected[a]
                for c in city_connected[b]:
                    city_group[c] = city_group[b]
                    city_connected[c] = city_connected[b]
            else:   # both a and b is not conected with machine
                city_connected[a] += city_connected[b]
                for c in city_connected[a]:
                    city_group[c] = city_group[a]
                    city_connected[c] = city_connected[a]
            #print(city_group)
            #print(city_connected)
    return totalDisconnected

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    try:
        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))

        machines = []

        for _ in range(k):
            machines_item = int(input())
            machines.append(machines_item)

        result = minTime(roads, machines)
    except:
        result = 8

    fptr.write(str(result) + '\n')

    fptr.close()
