class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, reachable_set):
            # Mark the current cell as reachable from the ocean
            reachable_set.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and the "reverse flow" condition (higher or equal)
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in reachable_set and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable_set)

       # Start DFS from Pacific boundaries (Top and Left), r = 0 or c = 0
        pacific_reachable_set = set()
        for c in range(cols):
            dfs(0, c, pacific_reachable_set)
        for r in range(rows):
            dfs(r, 0, pacific_reachable_set)

        # Start DFS from Atlantic boundaries (Bottom and Right), r = rows - 1 or c = cols - 1
        atlantic_reachable_set = set()
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable_set)
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable_set)

        # Find cells that are in both reachable sets
        return [list(coord) for coord in atlantic_reachable_set & pacific_reachable_set]
        