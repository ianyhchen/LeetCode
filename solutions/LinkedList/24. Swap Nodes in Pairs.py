# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy node to simplify head edge cases
        dummy = ListNode(0, head)
        dummy.next = head
        prev = dummy

        # Ensure there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Identify the two nodes to be swapped
            node1 = prev.next
            node2 = prev.next.next

            # Step 1: Connect previous part to the second node
            prev.next = node2
            # Step 2: Connect the first node to the rest of the list
            node1.next = node2.next
            # Step 3: Complete the swap by pointing node2 back to node1
            node2.next = node1

            # Move prev pointer two nodes ahead (to node1's new position)
            prev = node1
        
        return dummy.next

# Recursion
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # 1. Base Case: If less than 2 nodes, no swap possible       
            if not head or not head.next:
                return head

            # 2. Identify the nodes to swap
            first = head
            second = head.next

            # 3. Recursive Step: 
            # first.next should point to the result of swapping the rest of the list
            first.next = self.swapPairs(second.next)

            # 4. Swap current pair:
            # second node now points back to the first node
            second.next = first

            # 5. Return second node as the new head of this pair
            return second