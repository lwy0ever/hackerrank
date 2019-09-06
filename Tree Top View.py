

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    d = {}
    stack = [(root,0)]
    while stack:
        e = stack.pop(0)
        if e[1] not in d:
            d[e[1]] = e[0].info
        if e[0].left:
            stack.append((e[0].left,e[1] - 1))
        if e[0].right:
            stack.append((e[0].right,e[1] + 1))
    l = list(d.keys())
    l.sort()
    for e in l:
        print(d[e],end = ' ')

        


