# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertionSort(arr):
    ans = 0
    n = len(arr)
    for i in range(1,n):
        c = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > c:
            arr[j + 1] = arr[j]
            ans += 1
            j -=1
        arr[j + 1] = c
    return ans

def qs(arr,start,end):
    if end - start <= 1:
        return 0
    ans = 0
    c = arr[end - 1]
    ind = start
    for i in range(start,end - 1):
        if arr[i] <= c:
            arr[i],arr[ind] = arr[ind],arr[i]
            ind += 1
            ans += 1
    arr[ind],arr[end - 1] = arr[end - 1],arr[ind]
    #print(' '.join(map(str,arr)))
    ans += 1
    return qs(arr,start,ind) + qs(arr,ind + 1,end) + ans

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(insertionSort(arr[:]) - qs(arr[:],0,n))
