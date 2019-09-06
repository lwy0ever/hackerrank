# Enter your code here. Read input from STDIN. Print output to STDOUT
def qs(arr):
    n = len(arr)
    if n <= 1:
        return arr
    c = arr[0]
    left,right = [],[]
    for i in range(1,n):
        if c > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = qs(left)
    right = qs(right)
    print(' '.join(map(str,(left + [c] + right))))
    return left + [c] + right

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    qs(arr)
