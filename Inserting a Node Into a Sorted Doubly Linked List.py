

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if head == None:
        return node
    if data < head.data:
        node.next = head
        head.prev = node
        return node
    elif head.next == None:
        head.next = node
        node.prev = head
        return head
    cur = head
    while cur.next and cur.next.data < data:
        cur = cur.next
    node.next = cur.next
    node.prev = cur
    cur.next = node
    if cur.next:
        cur.next.prev = node
    return head



