import math
from functools import lru_cache 
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # Define the helper function inside the main method to isolate the cache
        @lru_cache(None)
        def dp(i, x, y):
            # Base Case
            if i == len(nums):
                if x == y and x > 0:
                    return 1
                else:
                    return 0
            # Subproblem transition (the recurrence relation)
            res1 = dp(i + 1, x, y)
            res2 = dp(i + 1, math.gcd(x, nums[i]), y)
            res3 = dp(i + 1, x, math.gcd(y, nums[i]))

            return (res1 + res2 + res3) % MOD

        return dp(0, 0, 0)