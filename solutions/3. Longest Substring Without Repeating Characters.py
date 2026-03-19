'''
Sliding window - Set
複雜度： O(n)（每個字元最多進出窗口各一次）
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        # Use a set to store characters in the current window        
        char_set = set()

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If s[right] is already in the set, move left pointer 
            # until s[right] is no longer in the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the current character and update max_len
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
            
'''
Sliding window - hashmap
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        # # char_map stores the last seen index of each character: {char: index}        
        char_map = {}
        
        for right in range(len(s)):  
            char = s[right]

            # If char is in map, it might be a repeating character
            if char in char_map:
                # Critical: Move left to the right of the last occurrence, 
                # but ONLY if the last occurrence is within the current window
                # 確保left 不會往回跑
                left = max(left, char_map[char] + 1)

            char_map[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
            