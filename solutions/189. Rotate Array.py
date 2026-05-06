# additional slice, Space complexity: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        n = len(nums)

        # Handle cases where k is greater than the length of the array
        k = k % n

        # Create a temporary array to store the rotated elements
        # Space complexity: O(n)
        temp = [0] * n

        # Calculate the new position for each element using modulo
        for i in range(n):
            target_index = (i + k) % n
            temp[target_index] = nums[i]
        
        # Copy the results back to the original array to satisfy in-place requirement
        # Note: nums[:] = temp is a more idiomatic Python way to do this
        nums[:] = temp        
        # for i in range(n):
        #     nums[i] = temp[i]


# 三次反轉法，Space complexity: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        n = len(nums)
        k = k % n

        # Helper function to reverse elements in-place
        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        # This moves the elements that should be at the front to the front area
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements to restore their original relative order
        reverse(0, k - 1)

        # Step 3: Reverse the remaining n-k elements to restore their order
        reverse(k, n - 1)