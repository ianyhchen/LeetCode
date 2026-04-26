# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node and point it to head
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy

        # 2. Move fast pointer n+1 steps forward
        # So that there is a gap of n nodes between fast and slow        
        for _ in range(n + 1):
            fast = fast.next

        # 3. Move both pointers until fast reaches the end (None)
        while fast:
            fast = fast.next
            slow = slow.next    
                    
        # 4. Now slow is at the (n+1)-th node from the end
        # Perform the deletion
        slow.next = slow.next.next

        return dummy.next


        
            
