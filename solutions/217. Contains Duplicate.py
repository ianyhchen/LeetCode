'''
Hash Set solution
time complexity of O(n) 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False

'''

'''
Sorting solution
time complexity of O(n log n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1) :
            if nums[i] == nums[i + 1]:
                return True
        return False    
'''

'''
check set length
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempSet = set(nums)
        return len(nums) > len(tempSet)
'''