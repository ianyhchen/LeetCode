class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize count (running sum) and max_len
        count, max_len = 0, 0

        # Initialize hash map with {prefix_sum: first_index}
        # We use {0: -1} to handle cases where the sub-array starts from index 0
        sum_map = {0: -1}

        for i in range(len(nums)):
            # Treat 1 as +1 and 0 as -1
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            # Only store the first occurrence to ensure maximum length
            if count not in sum_map:
                sum_map[count] = i
            else:
                # If this prefix sum has been seen before, calculate the length
                current_len = i - sum_map[count]
                max_len = max(max_len, current_len)

        return max_len

