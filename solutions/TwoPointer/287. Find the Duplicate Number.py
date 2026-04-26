class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point in the cycle
        # Initialize both pointers at the start (index 0)
        slow, fast = nums[0], nums[0]

        # Move tortoise by 1 step and hare by 2 steps
        # We use a 'do-while' logic here by moving them once before checking
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        while fast != slow:
            slow  = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]

        # Move both pointers 1 step at a time until they meet
        # The hare stays at the meeting point from Phase 1
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        # Both pointers meet at the entrance of the cycle
        return slow

