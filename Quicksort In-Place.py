# Enter your code here. Read input from STDIN. Print output to STDOUT
def qs(arr,start,end):
    if end - start <= 1:
        return
    c = arr[end - 1]
    ind = start
    for i in range(start,end - 1):
        if arr[i] <= c:
            arr[i],arr[ind] = arr[ind],arr[i]
            ind += 1
    arr[ind],arr[end - 1] = arr[end - 1],arr[ind]
    print(' '.join(map(str,arr)))
    qs(arr,start,ind)
    qs(arr,ind + 1,end)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    qs(arr,0,n)
