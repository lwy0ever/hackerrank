

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
        return head
    else:
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = node
        return head

