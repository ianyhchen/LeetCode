# BFS
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()

        # 1. 初始化：將所有 0 的座標入隊，並將 1 標記為未訪問（用 -1 表示）
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1 # 標記為尚未計算距離的 1

        #方向矩陣，將上下左右四個可能的位移量包在list內，方便迴圈使用
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 如果相鄰座標在邊界內，且是尚未訪問過的 1
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    # 距離等於當前座標距離 + 1
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat
    
# DP
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # initialization
        dist =[]
        for r in range(rows):
            current_row = []
            for c in range(cols):
                if mat[r][c] == 0:
                    current_row.append(0)
                else:
                    current_row.append(float('inf'))
            dist.append(current_row)

        # First scan, from top left to bottom right
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    if r > 0:
                        dist[r][c] = min(dist[r][c], dist[r - 1][c] + 1)
                    if c > 0:
                        dist[r][c] = min(dist[r][c], dist[r][c - 1] + 1)                    

        # Second scan, from bottom right to top left
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] != 0:          
                    if r < rows - 1:
                        dist[r][c] = min(dist[r][c], dist[r + 1][c] + 1)
                    if c < cols - 1:
                        dist[r][c] = min(dist[r][c], dist[r][c + 1] + 1)
        
        return dist