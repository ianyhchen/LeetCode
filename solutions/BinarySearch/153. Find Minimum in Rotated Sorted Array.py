class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Binary search continues as long as the search space has at least two elements
        # Why while left < right? 當搜尋區間縮小到剩下一個元素時，left 會等於 right，這時我們不需要再進迴圈判斷，直接回傳即可
        while left < right:
            mid = left + (right - left) // 2

            # If mid element is greater than the rightmost element, 
            # the pivot (minimum) must be in the right half (excluding mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than the rightmost element,
            # the pivot could be mid itself or in the left half
            elif nums[mid] < nums[right]:
                right = mid

        # When left == right, we have found the minimum element
        return nums[left]
