class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            value = nums[i]
            # Check if the number is in the valid range [1, n]
            # AND make sure the target position doesn't already have the correct number
            # This avoiding-duplicate check prevents infinite loops
            if 1 <= value <= n and nums[i] != nums[value - 1]:
                # Swap the elements to put 'value' into its correct bucket (index value - 1)
                nums[value - 1], nums[i] = nums[i], nums[value - 1]
            else:
                # Only move to the next index if no swap happened
                i += 1

        # Second pass: find the first index that doesn't match its expected value (i + 1)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # If all positions are correct, the missing integer is n + 1
        return n + 1