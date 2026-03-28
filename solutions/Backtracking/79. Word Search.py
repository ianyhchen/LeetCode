class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = False

        def dfs(w_index, r, c):
            # 1. 成功條件：如果索引達到單字長度，代表全數匹配成功
            if w_index == len(word):
                return True

            # 2. 失敗條件：越界、字元不匹配、或已訪問過
            if ( r < 0 or r >= rows or c < 0 or c >= cols or 
                word[w_index] != board[r][c]):
                return False            
           
            # Set current char to # as visited
            temp_val = board[r][c]
            board[r][c] = '#'

            #必須接收回傳值，只要有一個方向成功就回傳 True
            found = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc                
                if dfs(w_index + 1, nr, nc):
                    found = True
                    break
                    
            # 5. 回溯：離開這格前恢復原狀
            board[r][c] = temp_val
            return found
       
        for r in range(rows):
            for c in range(cols):                                              
                if dfs(0, r, c): 
                    return True                   

        return res
                        
        