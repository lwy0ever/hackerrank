

    def levelOrder(self,root):
        #Write your code here
        if root == None:
            return
        q = [root]
        for n in q:
            #if n:
            print(n.data,end = ' ')
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

