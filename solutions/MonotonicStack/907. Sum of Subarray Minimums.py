class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        # ple[i] stores the index of the previous strictly less element than arr[i]
        # Default to -1 if no such element exists
        ple = [-1] * n

        # nle[i] stores the index of the next less or equal element than arr[i]
        # Default to n if no such element exists
        nle = [n] * n
        
        # ---------------------------------------------------------
        # Pass 1: Find Previous Less Element (Strictly Less)
        # ---------------------------------------------------------
        stack = [] # Monotonic increasing stack storing indices
        for i in range(n):
            # Maintain monotonic increasing property
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # If stack is not empty, the top element is the previous less element
            if stack:
                ple[i] = stack[-1]
            stack.append(i)

        # ---------------------------------------------------------
        # Pass 2: Find Next Less Element (Less or Equal to avoid duplicates)
        # ---------------------------------------------------------
        stack = [] # Clear stack for the second pass
        for i in range(n):
            # Using >= ensures that the first duplicate to the right 
            # will correctly act as the right boundary for the previous duplicate
            while stack and arr[stack[-1]] >= arr[i]:
                popped_index = stack.pop()
                nle[popped_index] = i
            stack.append(i)

        # ---------------------------------------------------------
        # Pass 3: Calculate the total contribution of each element
        # ---------------------------------------------------------
        total_sum = 0
        for i in range(n):
            # Count of subarrays where arr[i] is the minimum on the left
            left_count = i - ple[i]
            # Count of subarrays where arr[i] is the minimum on the right
            right_count = nle[i] - i

            # Total subarrays contributed by arr[i] = left_count * right_count
            contribution = left_count * right_count * arr[i]
            
            total_sum  = (total_sum + contribution) % MOD
        
        return total_sum


