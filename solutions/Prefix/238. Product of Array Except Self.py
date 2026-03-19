# 左右乘積陣列法 (Standard O(n) Space)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. Initialize with fixed size to avoid IndexError
        prefix = [1] * n
        suffix = [1] * n        

        # Calculate prefix array
        # prefix[i] stores the product of all elements to the left of i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Calculate suffix array
        # suffix[i] stores the product of all elements to the right of i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]
    
# 空間優化法 (Optimized O(1) Space)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. Initialize with fixed size to avoid IndexError
        res = [1] * n  

        # Calculate prefix product directly into res
        # After this loop, res[i] contains product of all elements to the left
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Multiply by suffix product on the fly
        # We use a descriptive variable to keep track of the product of elements to the right
        right = 1
        for i in range(n - 1, -1, -1):
            # res[i] is already prefix, now multiply by suffix right
            res[i] = res[i] * right
            # Update right for the next element to the left
            right = right * nums[i]            

        return res