from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Check if the input list is empty
        if not nums:
            return ""

        # Define custom comparison logic
        def compare(s1, s2):
            # If concatenated s1+s2 is larger, s1 should come first (return -1)
            if s1 + s2 > s2 + s1:
                return -1
            elif s1 + s2 < s2 + s1:
                return 1
            else:
                return 0

        # Convert all integers to strings for concatenation and comparison
        nums_as_strings = [str(num) for num in nums]        
        
        # Sort using the custom comparator
        sorted_nums = sorted(nums_as_strings, key = cmp_to_key(compare))

        # Join the sorted strings
        res = ''.join(sorted_nums)

        # Edge case: if the largest number is "0", the entire result should be "0"
        # e.g., nums = [0, 0] -> result becomes "0" instead of "00"
        return res if res[0] != "0" else "0"
