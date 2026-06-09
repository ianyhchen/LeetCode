class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        left = max(1, n - k)
        right = n + k
        sum = 0
        for i in range(left, right + 1):           
            if n & i == 0:                
                sum += i
        return sum
            