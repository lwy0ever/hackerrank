

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    nodes = []
    cur = head
    while cur:
        if nodes.count(cur) > 0:
            return True
        nodes.append(cur)
        cur = cur.next
    return False

