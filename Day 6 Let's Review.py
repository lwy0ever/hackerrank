# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    S = input()
    print(S[0::2] + ' ' + S[1::2])
