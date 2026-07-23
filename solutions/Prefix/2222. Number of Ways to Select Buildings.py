class Solution:
    def numberOfWays(self, s: str) -> int:
        # Step 1: Count total occurrences of '0' and '1' in the string
        total_zero, total_one = 0, 0
        
        for c in s:
            if c == '0':
                total_zero += 1
            elif c == '1':
                total_one += 1

        # Step 2: Initialize counters for the left side
        left_zero, left_one = 0, 0
        ans = 0

        # Step 3: Iterate through each character as the middle element
        for c in s:
            # To form "101", we need '1' on the left and '1' on the right
            if c == '0':
                right_one = total_one - left_one
                ans += left_one * right_one

                # Update left counter for the next iterations
                left_zero += 1           
            else:
                 # To form "010", we need '0' on the left and '0' on the right
                right_zero = total_zero - left_zero
                ans += left_zero * right_zero
                
                # Update left counter for the next iterations
                left_one += 1
        
        return ans


