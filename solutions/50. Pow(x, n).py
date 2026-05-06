class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: any number to the power of 0 is 1
        if n == 0:
            return float(1)
        
        # Handle negative exponent: x^(-n) is equal to (1/x)^n
        if n < 0:
            n = -n
            x = 1 / x
        
        # Recursive step: divide the problem into half
        # This reduces the time complexity from O(n) to O(log n)
        half = self.myPow(x, n // 2)

        # If n is even: x^n = (x^(n/2))^2
        if n % 2 == 0:
            return half * half
        # If n is odd: x^n = (x^(n/2))^2 * x
        # We multiply by x one more time because n // 2 discards the remainder
        else:
            return half * half * x
