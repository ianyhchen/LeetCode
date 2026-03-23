# 須注意溢位檢查及進位

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        i = 0
        sign = 1 # 1: positive, -1: negetive 
        res = 0

        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Handle sign (only if it exists at the current position)
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Convert digits and handle overflow
        while i < n and s[i].isdigit():      
            digit = int(s[i])

            # Check overflow
            # INT_MAX = 2,147,483,647
            limit = INT_MAX // 10
            if res > limit or (res == limit and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            # Carry last digit
            res = res * 10 + digit
            i += 1

        return res * sign