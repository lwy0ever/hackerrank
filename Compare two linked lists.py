

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        else:
            llist1 = llist1.next
            llist2 = llist2.next
    if llist1 == None and llist2 == None:
        return 1
    else:
        return 0

