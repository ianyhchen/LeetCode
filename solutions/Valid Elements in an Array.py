class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return nums
            
        is_valid = [False] * n
        is_valid[0], is_valid[n - 1] = True, True
        left_max = nums[0]
        right_max = nums[n - 1]
        for i in range(1, n):
            if nums[i] > left_max:
                is_valid[i] = True
                left_max = nums[i]
        for i in range(n - 1, 0, -1):
            if nums[i] > right_max:
                is_valid[i] = True
                right_max = nums[i]

        return [nums[i] for i in range(n) if is_valid[i]]