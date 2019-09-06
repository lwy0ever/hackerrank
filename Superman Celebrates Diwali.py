# Enter your code here. Read input from STDIN. Print output to STDOUT

def superman(n,h,jump,arr):
    #print(arr)
    # dp[i][j] 表示第i栋楼，到第j层最多可以救援的人数（从底层开始推算）
    dp = [[0] * h for _ in range(n)]
    # ma[j]表示第j层最多可救援人数，也就是max(dp[0][j],dp[1][j]...)
    ma = [0] * h
    for i in range(n):
        # 最底层可救援最底层的人数
        dp[i][0] = arr[i][0]
        ma[0] = max(ma[0],dp[i][0])
    for j in range(1,h):
        for i in range(n):
            # 救援方案1：下层最大人数加上本层人数
            dp[i][j] = dp[i][j - 1] + arr[i][j]
            # 能否跳跃
            if j >= jump:
                # 从某一栋楼的j-jump层跳跃到j层
                dp[i][j] = max(dp[i][j],ma[j - jump] + arr[i][j])
            ma[j] = max(ma[j],dp[i][j])
    return ma[h - 1]
    '''
    ans = 0
    for i in range(n):
        ans = max(ans,dp[i][h - 1])
    return ans
    '''


if __name__ == '__main__':
    n,h,jump = list(map(int,input().split()))

    arr = [[0] * h for _ in range(n)]

    for i in range(n):
        p = list(map(int,input().split()))
        for l in p[1:]:
            arr[i][l - 1] += 1
    
    r = superman(n,h,jump,arr)
    print(r)
