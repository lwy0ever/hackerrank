""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check(node,small,big):
    if node:
        if node.data <= small or node.data >= big:
            return False
        else:
            return check(node.left,small,node.data) and check(node.right,node.data,big)
    return True
def check_binary_search_tree_(root):
    return check(root,-1,10 ** 4 + 1)
