'''
BFS solution
O(m * n) complexity
* 常見錯誤與陷阱
    - 起始時間計算：最後一波橘子腐爛後，隊列會再跑一次但不會再感染新橘子，要注意不要多加了最後那一分鐘。

    - 孤島問題：有些新鮮橘子被空格 0 包圍，永遠接觸不到腐爛橘子，必須透過最終的新鮮橘子計數器來判斷。

    - 空網格/無新鮮橘子：若網格一開始就全是 0 或全是 2，應回傳 0 而不是 -1

'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize: count fresh oranges and add all rotten ones to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # If no fresh oranges exist initially, 0 minutes have passed
        if fresh_count == 0:
            return 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        # Hint: fresh_count > 0 make sure not add more minute if the last orange was rotten but queue is not empty
        while queue and fresh_count > 0:
            minutes += 1

            # 關鍵：固定這一層的長度，保證這一分鐘內所有橘子同時擴散            
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # rotten 
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Final check: if fresh_count is 0, all oranges rotted
        return minutes if fresh_count == 0 else -1
            