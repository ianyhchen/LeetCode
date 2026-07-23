class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                area = 0
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 0
                    area += 1

                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                area += 1
                                grid[nr][nc] = 0
                                queue.append((nr, nc))                
                max_area = max(max_area, area)
        return max_area