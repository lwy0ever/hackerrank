

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter your code here
    cur = root
    while (v1 - cur.info) * (v2 - cur.info) > 0:
        if v1 < cur.info:
            cur = cur.left
        else:
            cur = cur.right
    return cur


