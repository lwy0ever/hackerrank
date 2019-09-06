

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    cur = head
    while position > 1:
        position -= 1
        cur = cur.next
    node.next = cur.next
    cur.next = node
    return head

