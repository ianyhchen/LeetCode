class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result variable to store the reversed bits
        res = 0

        # Since it's a 32-bit unsigned integer, we iterate exactly 32 times
        for i in range(32):
            # Extract the last bit (LSB) of n using AND mask
            bit = n & 1
            
            # Shift the result to the left to make room for the new bit
            res = res << 1
            
            # Combine the extracted bit into the result using OR operation
            res = res | bit
            
            # Shift n to the right to process the next bit in the next iteration
            n = n >> 1
        
        return res