# 計算攤平成一維陣列的index後轉換回二維
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:        
        rows, cols = len(grid), len(grid[0])
        total = rows * cols

        # Optimize k by taking the modulo of total elements to prevent unnecessary full rotations
        k = k % total

        # Initialize the result grid with the same dimensions
        ans = [[0] * cols for _ in range(rows)]

        # Iterate over every cell in the original grid
        for r in range(rows):
            for c in range(cols):
                # Convert 2D coordinates (r, c) into a flattened 1D index
                old_idx = r * cols + c

                # Calculate the new 1D index after shifting k positions cyclically
                new_idx = (old_idx + k) % total

                # Convert the new 1D index back to 2D coordinates (new_r, new_c)
                new_r = new_idx // cols
                new_c = new_idx % cols
                
                # Place the original element into its new mapped position
                ans[new_r][new_c] = grid[r][c]
        return ans

