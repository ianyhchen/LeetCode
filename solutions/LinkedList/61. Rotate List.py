# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: if the list is empty, return head immediately
        if not head:
            return head

        # Step 1: Calculate the length of the list and find the tail node
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1        

        # Step 2: Calculate effective rotations
        # If k is a multiple of n, no rotation is needed
        k = k % n
        if k == 0:
            return head

        # Step 3: Connect the tail to the head to form a circular linked list
        curr.next = head

        # Step 4: Find the new tail node
        # The new tail is at position (n - k - 1) from the current head
        new_tail = head
        steps = (n - k) - 1
        for _ in range(steps):
            new_tail = new_tail.next
        
        # Step 5: Set the new head and break the circular connection
        new_head = new_tail.next
        new_tail.next = None

        return new_head

