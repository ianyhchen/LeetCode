# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Compare two values from list 1 and list 2, 
then take the small value and create a new list.

Use dummy pointer which is always pointing to head node as a next node.
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val > list2.val:                
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        if list1:
            current.next = list1            
        if list2:
            current.next = list2
        return dummy.next