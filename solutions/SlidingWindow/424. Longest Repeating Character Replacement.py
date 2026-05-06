from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use a hash map to store the frequency of characters in the current window
        char_map = defaultdict(int)
        left, right, max_freq = 0, 0, 0

        # Expand the window using the right pointer
        while right < len(s):            
            char_map[s[right]] += 1
            # Update max_freq to reflect the highest frequency of any character seen so far in a window
            max_freq = max(max_freq, char_map[s[right]])
            # Current window size
            window_size = right - left + 1
            
            # If (window_size - max_freq) > k, the current window is invalid
            if window_size - max_freq > k:
                # Shrink the window from the left by 1 to maintain the maximum valid window size found so far
                char_map[s[left]] -= 1                
                left += 1

            right += 1
            
        # The maximum window size is preserved until the end
        return len(s) - left