
# Two pass solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1

        # Find the index of the smallest element (pivot)    
        pivot = self.findMinIndex(nums)

        # Determine which part to search
        # The pivot splits the array into two sorted parts: [0...pivot-1] and [pivot...n-1]
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            return self.binarySearch(nums, pivot, len(nums) - 1, target)
        else: 
            return self.binarySearch(nums, 0, pivot - 1, target)

    def findMinIndex(self, nums):
        length = len(nums)
        if length == 1:
            return 0    
        left, right = 0, length - 1

        while left < right:
            mid = left + (right - left)//2
            # If mid element is greater than the right element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is mid or to the left
                right = mid
        return left
    
    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1