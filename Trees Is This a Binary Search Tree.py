""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def check(root,mi,ma):
    if root.left:
        if root.left.data >= root.data or root.left.data <= mi:
            return False
    if root.right:
        if root.right.data <= root.data or root.right.data >= ma:
            return False
    return (check(root.left,mi,root.data) if root.left else True) and (check(root.right,root.data,ma) if root.right else True)
    
def checkBST(root):
    #print(root.data)
    return check(root,float('-inf'),float('inf'))
