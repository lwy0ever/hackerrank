#!/bin/python3

import os
import sys

#
# Complete the coinOnTheTable function below.
#
def coinOnTheTable(m, k, board):
    #
    # Write your code here.
    #
    n = len(board)
    dp = [[[float('inf')] * m for _ in range(n)] for _ in range(k + 1)]    # dp[k][i][j]表示用k步到达(i,j)需要最小的op次数
    # 为了方便,将坐标从(1,1)到(n,m),改为(0,0)到(n-1,m-1)
    # 递归方程
    # dp[0][0][0] = 0
    # dp[0][i][j] = float('inf')    i != 0 or j != 0
    # dp[k][i][j] = min(
    #    dp[k - 1][i - 1][j] + move(i - 1,j,i,j),
    #    dp[k - 1][i + 1][j] + move(i + 1,j,i,j),
    #    dp[k - 1][i][j - 1] + move(i,j - 1,i,j),
    #    dp[k - 1][i][j + 1] + move(i,j + 1,i,j))
    # move(x,y,i,j),如果(x,y)的方向符指向i,j,则move(x,y,i,j)=0,否则move(x,y,i,j)=1
    dp[0][0][0] = 0

    def move(r,c,tr,tc):
        if 0 <= r < n and 0 <= c < m:
            if (board[r][c] == 'U' and r - 1 == tr) or \
                (board[r][c] == 'D' and r + 1 == tr) or \
                (board[r][c] == 'L' and c - 1 == tc) or \
                (board[r][c] == 'R' and c + 1 == tc):
                    return 0
            else:
                return 1
        return float('inf')

    ans = float('inf')

    for l in range(1,k + 1):
        for i in range(n):
            for j in range(m):
                if move(i - 1,j,i,j) < float('inf'):
                    dp[l][i][j] = min(dp[l][i][j],dp[l - 1][i - 1][j] + move(i - 1,j,i,j))
                if move(i + 1,j,i,j) < float('inf'):
                    dp[l][i][j] = min(dp[l][i][j],dp[l - 1][i + 1][j] + move(i + 1,j,i,j))
                if move(i,j - 1,i,j) < float('inf'):
                    dp[l][i][j] = min(dp[l][i][j],dp[l - 1][i][j - 1] + move(i,j - 1,i,j))
                if move(i,j + 1,i,j) < float('inf'):
                    dp[l][i][j] = min(dp[l][i][j],dp[l - 1][i][j + 1] + move(i,j + 1,i,j))
                if board[i][j] == '*':
                    ans = min(ans,dp[l][i][j])
    return ans if ans != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    board = []

    for _ in range(n):
        board_item = input()
        board.append(board_item)

    result = coinOnTheTable(m, k, board)

    fptr.write(str(result) + '\n')

    fptr.close()
