# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
shop = dict(Counter(list(input().split(' '))).items())
#print(shop)
N = int(input())
customer = []
money = 0
for _ in range(N):
    c = list(input().split(' '))
    #print(c)
    if shop.get(c[0],0) > 0:
        shop[c[0]] -= 1
        money += int(c[1])
#print(customer)
print(money)
