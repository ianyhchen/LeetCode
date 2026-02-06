# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        if isBadVersion(1):
            return 1        
        while left < right:
            middle = left + (right - left)//2
            if isBadVersion(middle): #target < m
                right = middle                
            else:
                left = middle + 1
        return left
        