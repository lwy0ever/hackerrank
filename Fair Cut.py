#!/bin/python3

import os
import sys

#
# Complete the fairCut function below.
#
# 算法1，根据物理的“平衡定律law of equilibium”, 这道题相当于求一个电势平衡。
# The optimal cut is independent of the numbers, but only depends on their order. For example, if there are N=10 numbers to cut, and one person gets K=3 numbers, the best cut will be 0001010100, which means we first sort the 10 numbers in ascending order A[1]<=A[2]<=...<=A[10], and give the 0s to one person and the 1s to another. The strategy is to place the 01-string repetition (the "010101" in the example) as close to the middle of the whole string as possible. If K*2>N, redefine K to be N-K (switching the 0s and 1s). The intuition behind this greedy strategy comes from physics. The unfairness is like an interaction potential to be minimized. The 0s and 1s attract each other and form an ionic crystal in the middle of a positive charge background.
def fairCut(k, arr):
    ans = 0
    n = len(arr)
    arr.sort()
    if k > n / 2:
        k = n - k
    t = (n - 2 * k) // 2
    if n % 2 == 0:
        dig_str = '0' * t + '01' * k + '0' * t
    else:
        dig_str = '0' * (t + 1) + '10' * k + '0' * t
    I = [i for i in range(n) if dig_str[i] == '1']
    J = [i for i in range(n) if dig_str[i] == '0']
    return sum([abs(arr[i] - arr[j]) for i in I for j in J])
# 算法1结束

# 算法2，据说是背包问题，没看懂
#be equal to  (every number in  is less or equal than , so we know how to resolve absolute value). In the second case we will get to the state  and new function will be . The answer for the problem is .
#This approach gives us pseudo-polynomial solution but it's not enough for the problem. In the first approach we noticed that information about sum of Li's numbers is enough to recalculate the function. Also it's clear that we express function for the new state as linear combination of function for the old state and sum of Li's numbers in the old state. This thought pushes us to extend dp state in the another way:  minimal possible . To calculate  we should consider two cases: if the last integer is Li's and if it's Lu's. In the first case intended value is(similarly to the first approach). In the second case it is . Answer for the problem is . To obtain  solution we should notice that with fixed  and  we have only one interesting  (because in the end we are interested only in the state  and changing of  depends on changing of ).
def fairCut2(k,arr):
    n = len(arr)
    if k > n // 2:
        k = n - k
 
    # sort the array, so that when processing ith number in a, we know a[i] is
    # larger than or equal to previously processed numbers, so calculating abs
    # is easier
    arr.sort()
 
    # dp[i][j] is the value when ith number in a has already processed, and j of
    # those numbers assigned to li, initialize all value to maximum number
    dp = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
 
    # When i==0, j==0, no number assigned, the value is zero
    dp[0][0] = 0
 
 
    for i in range(0, n):  # iter through a
        # iter through the possiblities of sizes in li when a[i] needs to be
        # assigned
        for j in range(0, i + 1):
    
            # We ignore the cases when the number of li or lu larger than required
            if j > k or i - j > n - k:
                continue
    
            # There are two possiblities: (1)assign a[i] to li (2) or to lu
    
            # Possiblity (1) assign to li:
            # If a[i] would be assigned to li:
            #       all the numbers in lu needs to be substracted from a[i],
            #       so we add (i -j)* a[i] to d[i][j].
            #       Note: substraction of all lu has been done in prevous steps
            #       (see below, 3 lines later)
            #       (i-j) is the current number in lu.
            #
            #       a[i] WILL be substracted from all future a[x] assigned to lu,
            #       so we substract (n - k - (i - j))*a[i] from d[i][j]
            #       (n-k): size of lu in the final step,
            #       (i-j): current number in lu
            #       (n-k -(i-j)): size of remaining numbers to be assigned to lu
    
            temp_li = dp[i][j] + arr[i] * (i - j - (n - k - (i - j)))
    
            # Possiblity (2) assign to lu:
            # If a[i] would be assigned to lu:
            #       all the numbers in li needs to be substracted from a[i],
            #       so we add j* a[i] to d[i][j]
            #       Note: substraction of all lu has been done in prevous steps
            #       (see below, 2 lines later)
            #
            #       a[i] WILL be substracted from all future a[x] assigned to li,
            #       so we substract (k-j)*a[i] from d[i][j]
            #       (k-j) is the size of remaining numbers to be assigned to li
            temp_lu = dp[i][j] + arr[i] * (j - (k - j))
    
            # Possiblity (1), both sizes of assigned numbers and li increment by 1
            if dp[i + 1][j + 1] > temp_li:
                dp[i + 1][j + 1] = temp_li
    
            # Possiblity (2), size of assigned numbers increment by 1, size of li
            # remains the same
            if dp[i + 1][j] > temp_lu:
                dp[i + 1][j] = temp_lu
    
    return dp[n][k]
# 算法2结束

# 算法3，纯算，会超时
def unfairness(choosen,all):
    left = []
    cur = 0
    l = len(choosen)
    for i in range(len(all)):
        if cur < l and choosen[cur] == i:
            cur += 1
        else:
            left.append(i)
    #print(choosen,left)
    ans = 0
    for a in choosen:
        for b in left:
            ans += abs(arr[a] - arr[b])
    return ans

def fairCut3(k, arr):
    #
    # Write your code here.
    #
    ans = float('inf')
    arr.sort()
    n = len(arr)
    if k > n >> 1:
        k = n - k
    Li = []
    cur = 0
    lenLi = 0
    while True:
        if lenLi < k and cur + (k - lenLi) <= n:
            Li.append(cur)
            lenLi += 1
            cur += 1
        else:
            if lenLi == k:
                ans = min(ans,unfairness(Li,arr))
            cur = Li.pop()
            lenLi -= 1
            cur += 1
        #print(Li,cur,lenLi)
        if lenLi == 0 and cur + k > n:
            break
    return ans
# 算法3结束


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
