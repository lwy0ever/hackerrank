

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    pre = None
    cur = head
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    head = pre
    return head
    


