class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        # We look for the index 'i' such that nums[i] < nums[i + 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such an index is found, the sequence is not entirely descending
        if i >= 0:
            # Step 2: Find the element 'j' from the right that is just larger than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting from i + 1 to the end
        # This makes the suffix the smallest possible (ascending order)
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

