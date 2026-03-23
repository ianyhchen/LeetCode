# DFS solution
# Time & space complexity : O(m * n)
# Pros: 代碼簡潔，不需額外資料結構, Cons: 若島嶼形狀極端，遞迴可能過深
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            # Base case: if out of bounds or current cell is water ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # Mark the current land as visited by changing '1' to '0'
            # This prevents infinite loops and redundant counting
            grid[r][c] = '0'

            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Iterate through every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                # If we find land ('1'), it's the start of a new island
                if grid[r][c] == '1':
                    island_count += 1
                    # Use DFS to "sink" the entire island
                    dfs(r, c)

        return island_count
    

# BFS solution
# Worst space complexity: O(min(M, N))
# Pros: 不會發生 Stack Overflow，對大型網格更安全, Cons: 需額外維護 Queue 物件
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Iterate through every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                # If we find land ('1'), it's the start of a new island
                if grid[r][c] == "1":
                    island_count += 1
                    queue.append((r, c))
                    grid[r][c] = "0"

                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for i, j in directions:
                            nr, nc = curr_r + i, curr_c + j

                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1'):
                                queue.append((nr, nc))
                                grid[nr][nc] = "0"

        return island_count
