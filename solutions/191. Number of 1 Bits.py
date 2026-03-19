# 直觀，每次檢查最後一位（n & 1），然後右移。
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Keep checking until all bits are processed
        while n > 0:
            # Check if the last bit is 1 using bitwise AND with 1
            if n & 1:
                count += 1

            # Right shift n by 1 bit to process the next position
            # This is equivalent to n // 2            
            n >>=1
        
        return count
    
'''
 Brian Kernighan’s Algorithm   
使用 n & (n - 1)。這個運算會直接消掉二進位中最右邊的那個 1。
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Keep checking until all bits are processed
        while n > 0:           
            n = n & (n - 1)
            count += 1
        
        return count

