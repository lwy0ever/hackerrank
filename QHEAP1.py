# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heappush, heappop

heap = []
item_lookup = set()

for _ in range(int(input())):
    q = list(map(int,input().split()))
    if q[0] == 1:
        heappush(heap,q[1])
        item_lookup.add(q[1])
    elif q[0] == 2:
        item_lookup.discard(q[1])
    elif q[0] == 3:
        while heap[0] not in item_lookup:
            heappop(heap)
        print(heap[0])
    else:
        print('Error Type')
