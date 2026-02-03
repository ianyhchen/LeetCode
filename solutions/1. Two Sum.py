class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value:index
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[v] = i
        return []