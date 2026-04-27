"""
        Algorithm: Bit Manipulation - XOR (Exclusive OR)
        
        Key Properties of XOR:
        1. a ^ a = 0 (Any number XORed with itself is 0)
        2. a ^ 0 = a (Any number XORed with 0 remains unchanged)
        3. a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b (Commutative and Associative)
        
        Complexity:
        - Time: O(n) where n is the length of nums.
        - Space: O(1) as we only use a single variable for the result.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num
        
        return res