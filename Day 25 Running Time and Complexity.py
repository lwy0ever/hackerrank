# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print('Not prime')
        continue
    if n == 2:
        print('Prime')
        continue
    if n % 2 == 0:
        print('Not prime')
        continue
    for i in range(3,int(n ** 0.5) + 1,2):
        if n % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')
