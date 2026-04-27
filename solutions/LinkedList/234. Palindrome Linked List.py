# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: empty list or single node
        if not head or not head.next:
            return True

        # Step 1: Find the middle node using slow and fast pointers
        # After the loop, 'slow' will be at the start of the second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        # 'prev' will eventually become the head of the reversed second half
        prev = None
        curr = slow

        while curr:
            temp = curr.next    # Store next node
            curr.next = prev    # Reverse current node's pointer
            prev = curr         # Move prev forward
            curr = temp         # Move curr forward
        
        # Step 3: Compare the first half and the reversed second half
        # 'prev' starts from the end of original list, 'head' starts from the front
        left, right = head, prev
        while right:                # Only need to compare until the shorter half ends
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
