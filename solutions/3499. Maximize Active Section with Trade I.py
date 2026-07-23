# Run-Length Encoding 陣列解法
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Step 1: Run-Length Encoding (RLE) compression
        # Compress consecutive identical characters into (char, length) tuples        
        rle = []
        for c in s:
            if not rle or rle[-1][0] != c:
                rle.append([c, 1])
            else:
                rle[-1][1] += 1

        # Step 2: Calculate total initial '1's
        total_ones = sum(length for char, length in rle if char == "1")

        # Step 3: Scan triplets of (0-block, 1-block, 0-block)
        max_gain = 0
        for i in range(1, len(rle) - 1):
            # Check if the current block is '1' surrounded by '0' blocks
            if rle[i][0] == "1" and rle[i - 1][0] == '0' and rle[i + 1][0] == '0':
                left_zero = rle[i - 1][1]
                right_zero = rle[i + 1][1]

                # Net gain when merging these two '0' blocks
                max_gain = max(max_gain, left_zero + right_zero)
        # Step 4: Return maximum active sections possible
        return total_ones + max_gain
                        

