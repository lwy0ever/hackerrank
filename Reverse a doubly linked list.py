

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    cur = head
    while cur:
        cur.next,cur.prev = cur.prev,cur.next
        head = cur
        cur = cur.prev
    return head
    '''
    cur = head
    if not cur or not cur.next:
        return head
    nex = cur.next
    cur.next = None
    while cur and nex:
        tmp = nex.next
        cur.prev,nex.next = nex,cur
        cur = nex
        nex = tmp
    cur.prev = None
    return cur
    '''


