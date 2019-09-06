# Enter your code here. Read input from STDIN. Print output to STDOUT

def countingSort(arr):
    cnt = [0] * 100
    for a in arr:
        cnt[a] += 1
    ans = [cnt[0]]
    for i in range(1,100):
        ans.append(ans[i - 1] + cnt[i])
    return ans

if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        e = input().split()
        arr.append(int(e[0]))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
