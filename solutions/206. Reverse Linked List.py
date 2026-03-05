# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next  # Store the next node
            head.next = node  # Reverse the pointer
            node = head  # Move node forward
            head = temp  # Move head forward

        return node
