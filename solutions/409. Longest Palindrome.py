class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashtable = {}
        # Count frequencies
        for i in s:
            hashtable[i] = hashtable.get(i, 0) + 1
        has_odd_frequency = False
        count = 0
        for v in hashtable.values():
            # Check if the frequency is even
            if v % 2 == 0:
                count += v
            else:
                # If the frequency is odd, one occurrence of the
                # character will remain without a match
                count += v - 1
                has_odd_frequency = True
        # If has_odd_frequency is true, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if has_odd_frequency:
            return count + 1
        return count
