class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Get the number of unique non-zero numbers
        num_set = set(nums)
        return len(num_set) if 0 not in num_set else len(num_set) - 1