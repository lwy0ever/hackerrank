

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    stack = [root]
    while stack:
        n = stack.pop(0)
        print(n,end = ' ')
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)

