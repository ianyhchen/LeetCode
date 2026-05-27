class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        # Use absolute value to avoid Python's modulo behavior on negative numbers
        temp_x = abs(x)

        # Define 32-bit signed integer boundaries
        MAX = 2**31 - 1
        MIN = -2**31
        while temp_x != 0:
            pop = temp_x % 10
            temp_x //= 10

            # Check overflow before updating res
            # Since we use absolute value, we only need to compare with MAX // 10
            if res > MAX // 10 or (res == MAX // 10 and pop > 7):
                return 0

            res = res * 10 + pop            
        
        result = -res if x < 0 else res
        
        # Final check for the negative boundary -2147483648
        if result < MIN or result > MAX:
            return 0
        
        return result
