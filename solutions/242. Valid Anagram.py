# Sorting, O(n log n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t
        
        

# Hastable O(n)
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
            
        for v in counter.values():
            if v != 0:
                return False     

        return True
        
        