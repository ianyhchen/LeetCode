# String reverse
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False    

        s = str(x)
        reversed_s = ''.join(reversed(s))

        return s == reversed_s 

# 反轉一半數字
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False    

        revertedNumber = 0

        while x > revertedNumber:
            pop = x % 10
            revertedNumber = revertedNumber * 10 + pop
            x = x // 10
            
        # handle even or odd length
        return x == revertedNumber or x == revertedNumber // 10