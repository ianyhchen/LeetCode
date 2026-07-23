class Solution:
    def countSubstrings(self, s: str) -> int:
        # Helper function to expand around the given center indices.
        # It directly accesses the outer variable 's' without explicit passing.
        def palindromic_count(left: int, right: int) -> int:
            counter = 0

            # Expand outward as long as it's within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:            
                counter += 1
                left -= 1
                right += 1
            
            return counter

        # Iterate through each character, treating it as the center of potential palindromes
        total_count = 0
        for i in range(len(s)):
            # Case 1: Odd length palindromes (center is a single character e.g., "aba")
            total_count += palindromic_count(i, i)
            # Case 2: Even length palindromes (center is the gap between two characters e.g., "abba")
            total_count += palindromic_count(i, i +1)
        
        return total_count