

    def insert(self,head,data): 
        #Complete this method
        #self.display(head)
        n = Node(data)
        if head:
            #print('head:',end = '')
            #print(head.data,head.next)
            c = head
            while c.next:
                c = c.next
            c.next = n
            return head
        else:
            return n

