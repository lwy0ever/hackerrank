

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    distance = 0
    forward = head
    afterward = head
    while forward:
        forward = forward.next
        if distance > positionFromTail:
            afterward = afterward.next
        distance += 1
    return afterward.data
    '''
    l = []
    while head:
        l.append(head)
        head = head.next
    return l[-positionFromTail-1].data
    '''

