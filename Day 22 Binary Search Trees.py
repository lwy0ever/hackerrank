

    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1
        return max(self.getHeight(root.left) + 1,self.getHeight(root.right) + 1)

