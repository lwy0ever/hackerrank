#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    edges = {node:dict() for node in range(1,road_edges + 1)}

    for _ in range(road_edges):
        f,t,w = map(int,input().split())
        edges[f][t] = w

    questions = [tuple(map(int,input().split())) for _ in range(int(input()))]

    # 使用questions_dict存储需要记录的起止点对
    questions_dict = defaultdict(set)
    for f,t in questions:
        questions_dict[f].add(t)
    
    answers = dict()
    # 逐个起点计算
    for qf,qt in questions_dict.items():
        visited = {qf}
        # distance[i]表示起点为qf的情况下,到达i的距离
        distance = {node:-1 for node in range(1,road_nodes + 1)}
        distance[qf] = 0
        # bfs
        while visited:
            new_visited = set()
            for f in visited:
                disPre = distance[f]
                for t,w in edges[f].items():
                    dis = disPre + w
                    if distance[t] == -1 or dis < distance[t]:
                        distance[t] = dis
                        new_visited.add(t)
            visited = new_visited
        # 存储各个终点
        for t in qt:
            answers[(qf,t)] = distance[t]
    for f,t in questions:
        print(answers[(f,t)])
