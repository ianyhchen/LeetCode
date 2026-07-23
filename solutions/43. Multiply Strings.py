class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        # The product of two numbers of length L1 and L2 will have at most L1 + L2 digits
        res = [0] * (l1 + l2)

        # Iterate from right to left (least significant digit to most significant digit)
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1): 
                # Multiply current digits from num1 and num2
                mul = int(num1[i]) * int(num2[j])
                # Add the multiplication result to the existing value at the target position
                sum_val = mul + res[i + j + 1]
                # Update the current position with the units digit of the sum
                res[i + j + 1] = sum_val % 10
                # Carry over the tens digit of the sum to the next position on the left
                res[i + j] += sum_val // 10

        # Find the first non-zero digit to skip leading zeros    
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        
        # If all digits are zero, return "0". Otherwise, join and return the slice.
        return ''.join(map(str, res[start:])) if start < len(res) else "0"
