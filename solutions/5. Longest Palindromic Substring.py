'''
Time complexity: O(n**2)
Space: O(n), due to python slicing

從中心同時往左右擴散尋找相同字元，注意奇數&偶數情形
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:        

        def expand(left, right) -> str:
            # 只要在範圍內且字元相同，就繼續往外擴張            
            while left >= 0 and right < len(s) and s[left] == s[right]:                
                left -= 1
                right += 1               
            # 迴圈結束後，回傳這一段切下來的字串
            return s[left + 1: right]        

        res = ""

        for i in range(len(s)):
            # 奇數長度 (例如 "aba")
            odd = expand(i, i)
            # 偶數長度 (例如 "abba")
            even = expand(i, i + 1)

            if len(odd) > len(res): res = odd
            if len(even) > len(res): res = even

            ## 直接在 odd, even, 與當前的 res 中選出最長的一個
            # res = max(res, expand(i, i), expand(i, i + 1), key=len)

        return res

            