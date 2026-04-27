# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointer solution
        # slow moves one step and fast moves two steps
        # if there is a cycle, the fast pointer will eventually catch up to the slow pointer
        if head is None:
            return False
        fast = head
        slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
'''
Set solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set solution
        visited_nodes = set()
        curr = head
        while curr:
            if curr in visited_nodes:
                return True
            visited_nodes.add(curr)
            curr = curr.next
        return False
'''