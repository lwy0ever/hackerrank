class Graph:
    def __init__(self,n):
        self.node = [-1] * n
        self.edge = {i:set() for i in range(n)}
        self.width = 6

    def connect(self,x,y):
        self.edge[x].add(y)
        self.edge[y].add(x)
    
    def find_all_distances(self,start):
        self.node[start] = 0
        pos = {start}
        visited = {start}
        while pos:
            newPos = set()
            for p in pos:
                for np in self.edge[p]:
                    if np not in visited:
                        newPos.add(np)
                        visited.add(p)
                        if self.node[np] == -1:
                            self.node[np] = self.node[p] + self.width
                        else:
                            self.node[np] = min(self.node[np],self.node[p] + self.width)
            pos = newPos
            #print(pos,self.node,visited)
        self.node.pop(start)
        print(' '.join(map(str,self.node)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    #print(graph.edge)
    s = int(input())
    graph.find_all_distances(s-1)

