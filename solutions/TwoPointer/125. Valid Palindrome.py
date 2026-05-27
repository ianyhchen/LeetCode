class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        # Only need to loop while left pointer is strictly less than right pointer
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers towards the center
            left += 1
            right -= 1
            
        # If pointers meet without any mismatch, it's a valid palindrome
        return True 