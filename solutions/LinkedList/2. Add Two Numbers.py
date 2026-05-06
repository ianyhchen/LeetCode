# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:      
        # Initialize a dummy head to simplify the creation of the result list
        dummy = ListNode(0)
        # 'current' acts as a pointer to the last node in the result list
        current = dummy
        # 'carry' stores the value that overflows to the next decimal place
        carry = 0

        # Continue looping as long as there are nodes to process or a carry exists
        while l1 or l2 or carry != 0:
            # Extract values from current nodes, default to 0 if the list has ended
            # # Advance l1 and l2 pointers if they are not None
            l1_val, l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next

            # Calculate the sum for the current position
            sum = l1_val + l2_val + carry
            # Update carry for the next iteration (1 if sum >= 10, else 0)       
            carry = sum // 10

            # Create a new node with the digit at the current position
            new_node = ListNode(sum % 10)
            # Connect the new node to the result list
            current.next = new_node
            # Move the 'current' pointer forward to the newly created node
            current = current.next        
                        
        # The result starts from the node following the dummy head
        return dummy.next