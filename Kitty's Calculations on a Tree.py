# unfinished version

# Enter your code here. Read input from STDIN. Print output to STDOUT
#from collections import defaultdict
from itertools import combinations
def calculationsOnTree(father,childLevel,s):
    mod = 10 ** 9 + 7
    if len(s) == 1:
        print(0)
        return
    ans = 0
    for comb in combinations(s,2):
        a,b = comb
        #print(a,b)
        dis = 0
        while childLevel[a] < childLevel[b]:
            b = father[b]
            dis += 1
        while childLevel[a] > childLevel[b]:
            a = father[a]
            dis += 1
        while a != b:
            a = father[a]
            b = father[b]
            dis += 2
        #print(dis,comb)
        ans += dis * comb[0] * comb[1]
    print(ans % mod)


if __name__ == '__main__':
    n,q = list(map(int,input().split()))
    edges = set()
    #edict = defaultdict(set)
    dist = [[0] * (n + 1) for _ in range(n + 1)]
    fathered = set()
    a,b = list(map(int,input().split()))
    dist[a][b] = 1
    dist[b][a] = 1
    fathered.add(a)
    fathered.add(b)
    for _ in range(1,n - 1):
        a,b = list(map(int,input().split()))
        #edges.append(a,b)
        if a in fathered:
            for ff in fathered:
                dist[b][ff] = dist[a][ff] + 1
                dist[ff][b] = dist[ff][a] + 1
            fathered.add(b)
        elif b in fathered:
            for ff in fathered:
                dist[a][ff] = dist[b][ff] + 1
                dist[ff][a] = dist[ff][b] + 1
            fathered.add(a)
        else:   # neither a or b in fathered
            edges.add((a,b))
    while edges:
        for a,b in edges:
            if a in fathered:
                for ff in fathered:
                    dist[b][ff] = dist[a][ff] + 1
                    dist[ff][b] = dist[ff][a] + 1
                    edges.remove((a,b))
                fathered.add(b)
            elif b in fathered:
                for ff in fathered:
                    dist[a][ff] = dist[b][ff] + 1
                    dist[ff][a] = dist[ff][b] + 1
                    edges.remove((a,b))
                fathered.add(a)
    #for d in dist:
    #    print(d)
    mod = 10 ** 9 + 7
    for _ in range(q):
        qnum = input()
        #sets.append(list(map(int,input().split())))
        s = list(map(int,input().split()))
        if qnum == '1':
            print(0)
            continue
        ans = 0
        for a,b in combinations(s,2):
            #print(a,b)
            ans += dist[a][b] * a * b
        print(ans % mod)
    '''
    n,q = list(map(int,input().split()))
    edges = []
    edict = defaultdict(list)
    for _ in range(n - 1):
        a,b = list(map(int,input().split()))
        #edges.append(a,b)
        edict[a].append(b)
        edict[b].append(a)
    #print(edges)
    fathered = {1}
    toFindChild = {1}

    father = [0] * (n + 1)
    childLevel = [0] * (n + 1)
    while toFindChild:
        new_toFindChild = []
        for f in toFindChild:
            for child in edict[f]:
                if child not in fathered:
                    father[child] = f
                    childLevel[child] = childLevel[f] + 1
                    new_toFindChild.append(child)
                fathered.add(child)
        toFindChild = new_toFindChild
        #print(fathered,toFindChild,father)
    #print(father)
    #print(childLevel)

    #sets = []
    for _ in range(q):
        qnum = input()
        #sets.append(list(map(int,input().split())))
        calculationsOnTree(father,childLevel,list(map(int,input().split())))
    #print(sets)
    '''
