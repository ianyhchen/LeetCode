class Solution:
    def checkValidString(self, s: str) -> bool:
        # c_min and c_max represent the range of possible open '(' remaining.
        c_min, c_max = 0, 0
        
        for c in s:
            if c == '(':
                # '(' definitely increases both the lower and upper bounds
                c_min += 1
                c_max += 1
            elif c == ')':
                # ')' definitely decreases both the lower and upper bounds
                c_min -= 1
                c_max -= 1
            else:
                # '*' can be ')', which decreases c_min, or '(', which increases c_max
                c_min -= 1
                c_max += 1

            # Dynamic Adjustment 1: c_min cannot be negative.
            # If c_min < 0, it means we treated too many '*' as ')'. 
            # We fix this by treating some '*' as empty strings instead.
            if c_min < 0:
                c_min = 0
            
            # Dynamic Adjustment 2: If c_max < 0, it means even if we treat all '*' as '(',
            # we still don't have enough '(' to balance the ')'. Thus, it's impossible.
            if c_max < 0:
                return False
        # If the minimum possible remaining open '(' is 0, the string can be valid
        return c_min == 0