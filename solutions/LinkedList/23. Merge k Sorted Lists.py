import heapq
from typing import List, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Heap solution, time complexity: O(N* logK), space: O(K)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize the min-heap to store (value, index, node)
        # Using index as a tie-breaker to avoid comparing ListNode objects directly
        min_heap = []

        # Push the head of each linked list into the heap
        for i in range(len(lists)):
            node = lists[i]
            if node:
                # Store node.val for sorting, i for uniqueness, and node for retrieval
                heappush(min_heap, (node.val, i, node))

        # Dummy node acts as the starting point of the merged list
        dummy = ListNode()
        curr = dummy

        # Continue until there are no nodes left in the heap
        while min_heap:
            # Pop the node with the smallest value
            val, index, node = heappop(min_heap)

            # Connect the smallest node to the resulting list
            curr.next = node

            # If the popped node has a successor, push it into the heap
            if node.next:
                heappush(min_heap, (node.next.val, index, node.next))
            # Move the pointer forward in the merged list
            curr = curr.next
            
        # Return the head of the merged list (skipping dummy)
        return dummy.next
    
# Divide and conquer, time complexity: O(N* logK), space: O(logK)
from typing import List, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Helper function to merge two sorted linked lists
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            curr = dummy

            # Compare nodes from both lists and attach the smaller one
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            # If one list is exhausted, attach the remainder of the other list
            curr.next = list1 or list2
            
            return dummy.next

        # Helper function to divide and conquer the lists array
        def mergeK(lists, start, end):
            # Base Case: Single list remaining
            if start == end:
                return lists[start]
            # Base Case: No lists to merge
            if start > end:
                return None

            # Divide: Find the midpoint
            mid = (start + end) // 2

            # Conquer: Recursively merge the left and right halves
            left = mergeK(lists, start, mid)
            right = mergeK(lists, mid + 1, end)

            # Combine: Merge the two sorted halves
            return mergeTwoLists(left, right)
            
        # Start the recursive process for the entire range of lists
        return mergeK(lists, 0, len(lists) - 1)