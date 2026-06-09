class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        #找到規律，i = 1 + dp[i - offset], offset 在遇到2的次方會改變
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
    
# O(n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def count(num):
            b = 0
            while num > 0:
                num = num & (num - 1)
                b += 1
            return b
        
        for i in range(n + 1):
            b_count = count(i)
            res.append(b_count)
        
        return res

#O(n) 利用最低有效位元 (Least Significant Bit, LSB)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            res[i] = res[i & (i - 1)] + 1
        
        return res