class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # slow pointer tracks the position where the next non-zero element should be placed
        # fast pointer iterates through the entire array
        slow, fast = 0, 0

        while fast < len(nums):
            # When we find a non-zero element with the fast pointer
            if nums[fast] != 0:
                # Swap the non-zero element at 'fast' with the element at 'slow'
                # This moves non-zero elements forward and zeroes backward
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # Increment slow pointer to the next available position
                slow += 1
            # Always move the fast pointer to check the next element
            fast += 1
        