

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position == 0:
        return head.next
    cur = head
    while position > 1:
        position -= 1
        cur = cur.next
    cur.next = cur.next.next
    return head

