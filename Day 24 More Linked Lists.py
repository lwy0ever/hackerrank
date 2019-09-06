

    def removeDuplicates(self,head):
        #Write your code here
        if head == None:
            return None
        else:
            aHead = head
            aNext = aHead.next
            while aNext:
                if aHead.data == aNext.data:
                    aHead.next = aNext.next
                else:
                    aHead = aHead.next
                aNext = aHead.next
        return head
                

