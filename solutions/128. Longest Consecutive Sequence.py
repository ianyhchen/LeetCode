class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) lookups and handle duplicates
        hashSet = set(nums)
        max_len = 0

        for num in hashSet:
            # Only start counting if 'num' is the beginning of a sequence            
            if num - 1 not in hashSet:
                current_num = num
                current_length = 1

                # Incrementally check for the next numbers in the sequence
                while current_num + 1 in hashSet:
                    current_num += 1
                    current_length += 1

                # Update the global maximum length found so far
                max_len = max(max_len, current_length)                   
        
        return max_len
