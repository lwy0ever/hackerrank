

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    appeared = []
    while head1:
        appeared.append(head1)
        head1 = head1.next
    while head2:
        if appeared.count(head2) > 0:
            return head2.data
        head2 = head2.next

