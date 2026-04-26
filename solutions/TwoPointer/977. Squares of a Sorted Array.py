# 暴力解
# Time complexity: O(n log n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            res.append(i * i)
        res.sort()
        
        return res

# Two pointer   
# 負數平方後會變大，因此平方後的極大值會分布在原陣列的兩端（左側極大負數或右側極大正數） 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Pre-allocate the list to avoid dynamic resizing and the need to reverse
        res = [0] * n
        left, right = 0, n - 1
        
        # Fill the array from the back to the front (largest to smallest)
        pos = n - 1

        while left <= right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            if left_squared > right_squared:
                res[pos] = left_squared
                left += 1
            else:
                res[pos] = right_squared
                right -= 1

            pos -= 1       
        
        return res