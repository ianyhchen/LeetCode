# Hashtable solution
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_mapping = {}
        curr = head        
        # First pass: Create all new nodes without connections
        while curr:            
            if curr not in node_mapping:
                node_mapping[curr] = Node(curr.val)
            curr = curr.next
            
        # Second pass: Connect next and random pointers
        curr = head        
        while curr:            
            if curr.random:
                node_mapping[curr].random = node_mapping[curr.random]
            if curr.next:
                node_mapping[curr].next = node_mapping[curr.next]
            curr = curr.next
            
        return node_mapping[head]

#O(1) solution
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interleave cloned nodes within the original list
        curr = head 
        while curr:
            new_node = Node(curr.val)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            curr = new_node.next

        # Step 2: Copy the random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the interleaved list using a dummy node
        dummy = Node(0)
        copy_curr = dummy
        curr = head
        while curr:            
            copy_node = curr.next
            # Restore the original list's next pointer
            curr.next = copy_node.next

            # Connect the cloned nodes together
            copy_curr.next = copy_node
            
            # Move both pointers forward
            curr = curr.next
            copy_curr = copy_curr.next        
            
        return dummy.next
