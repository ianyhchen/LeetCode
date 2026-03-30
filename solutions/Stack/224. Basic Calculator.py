class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0     # Current cumulative result in the current scope
        sign = 1    # Current operator sign (1 for '+', -1 for '-')
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = 0
                # 重點
                # 用一個內層迴圈把完整的數字跑完
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # 此時 num 就是完整的數字（如 421），記得 i 已經往後移了，要繼續外層迴圈
                # 處理完數字後，這裏可以直接套用 sign 進行運算
                res += sign * num
                continue # 跳過後面的 i += 1，因為內層已經移過了
            
            elif char == '+':
                sign = 1

            elif char == '-':
                sign = -1

            elif char == '(':
                # Push the result calculated so far and the sign before the parenthesis
                # The order of pushing matters for popping later (LIFO)
                stack.append(sign)
                stack.append(res)
                # Reset res and sign for the new scope inside the parenthesis
                res = 0
                sign = 1

            elif char == ')':
                # The parenthesis scope ends. Pop the sign and the previous result.
                # Since we pushed (res, sign), we pop (sign, res).             
                old_res = stack.pop()
                old_sign = stack.pop()
                
                # 重點
                # Update the result: previous_total + (sign_before_bracket * bracket_result)              
                res = old_res + old_sign * res                

            # If char is a space ' ', it will simply be skipped by this increment
            i += 1
        
        return res
