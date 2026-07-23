"""
逆向感染法 : 從四個邊界的 'O' 出發進行 BFS/DFS。所有能被邊界 'O' 擴散延伸到的 'O'，都是「安全、不會被翻轉的」
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Edge case: if the board is smaller than 3x3, no cells can be fully surrounded
        if rows < 3 or cols < 3:
            return
        
        queue = deque()

        # Step 1: Scan top and bottom rows (including corners)
        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "#" # Mark as visited immediately
            if board[rows - 1][c] == "O":
                queue.append((rows - 1, c))
                board[rows - 1][c] = "#"

        # Step 2: Scan left and right columns (excluding corners to avoid duplicates)        
        for r in range(1, rows - 1):
            if board[r][0] == "O":
                queue.append((r, 0))
                board[r][0] = "#"
            if board[r][cols - 1] == "O":
                queue.append((r, cols - 1))
                board[r][cols - 1] = "#"
        
        # Step 3: BFS to propagate the "#" tag to all connected internal 'O's
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # If a neighboring 'O' is found, it's connected to the border and thus safe
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "#" # Mark immediately before pushing to queue
                    queue.append((nr, nc))       
                
        # Step 4: Final traversal to flip captured 'O's to 'X's, and restore safe '#'s back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"       # These 'O's were never reached by BFS (captured)
                elif board[r][c] == "#":
                    board[r][c] = "O"       # Restore the safe border-connected cells
