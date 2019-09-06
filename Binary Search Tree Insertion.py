

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        n = Node(val)
        if self.root == None:
            self.root = n
            return
        cur = self.root
        while cur:
            if val > cur.info:
                if cur.right == None:
                    cur.right = n
                    break
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = n
                    break
                else:
                    cur = cur.left
        else:
            cur = n


