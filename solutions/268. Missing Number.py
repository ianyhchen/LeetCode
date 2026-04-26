# 求和, time complexity: O(n), space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # total = 0
        # for i in range(len(nums) + 1):
        #     total += i
        
        # for i in nums:
        #     total -= i
        
        # return total

        return sum(range(len(nums) + 1)) - sum(nums)

# Set Solution, time and space complexity: O(n)  
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        hashSet = set(nums)

        for i in range(len(nums) + 1):
            if i not in hashSet:
                return i
            

'''
XOR solution

要理解這個解法，你只需要記住 XOR的三個神奇性質：
    - 歸零律：任何數字跟自己 XOR 都等於 0。x ^ x = 0
    - 恆等律：任何數字跟 0 XOR 都等於自己。x ^ 0 = x 
    - 交換律與結合律：運算的順序不影響結果。a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize res with n, because range(n) only goes up to n-1        
        n = len(nums)
        res = n

        # XOR every index and every value in the array
        for i in range(n):
            # res = res ^ i ^ nums[i]
            res ^= i ^ nums[i]

        return res
        