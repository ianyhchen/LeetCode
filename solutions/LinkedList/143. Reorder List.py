# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle of the linked list using slow and fast pointers
        # When fast reaches the end, slow will be at the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list into two halves and reverse the second half
        # 'mid' is the start of the second half
        mid = slow.next
        # Important: Disconnect the first half from the second half to avoid cycles
        slow.next = None

        # Standard in-place reversal of the second half
        prev_node = None
        curr_node = mid
        # reverse the half right part
        while curr_node:
            temp = curr_node.next       # Store next node
            curr_node.next = prev_node  # Reverse the pointer
            prev_node = curr_node       # Move prev forward
            curr_node = temp            # Move curr forward
        
        # 3. Merge the two halves (first half and reversed second half)
        # 'node' (now prev_node) is the head of the reversed second half
        left, right = head, prev_node

        while right:
            # Store the next nodes of both lists to prevent losing the reference
            left_next, right_next = left.next, right.next

            # Re-wire pointers to weave the nodes together
            left.next = right
            right.next = left_next

            # Move pointers forward for the next iteration
            left = left_next
            right = right_next
            


# Deque解法
from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        queue = deque()
        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next
        
        curr = queue.popleft()
        while queue:
            right_node = queue.pop()
            curr.next = right_node
            curr = right_node
            if queue:
                left_node = queue.popleft()
                curr.next = left_node
                curr = left_node
        
        if curr:
            curr.next = None
        














