

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    cur1 = head1
    cur2 = head2
    if cur1.data < cur2.data:
        head = cur1
        cur1 = cur1.next
    else:
        head = cur2
        cur2 = cur2.next
    cur = head
    while cur1 and cur2:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur2 = cur2.next
        cur = cur.next
    if cur1:
        cur.next = cur1
    if cur2:
        cur.next = cur2
    return head



