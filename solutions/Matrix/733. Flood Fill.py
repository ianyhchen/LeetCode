class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        # 如果新舊顏色一樣，直接回傳，避免死迴圈
        if original_color == color:
            return image

        len_r, len_c = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # 1. 檢查基本邊界（是否出界）
            if r < 0 or r >= len_r or c < 0 or c >= len_c:
                return
            # 2. 檢查顏色（是否不是原色，或已經被染成新顏色）
            if image[r][c] != original_color or image[r][c] == color:
                return
            # 染色
            image[r][c] = color
            
            # 向四個方向擴散
            for dr, dc in directions:
                nr, nc = r + dr, c + dc                
                dfs(nr, nc)
            
        dfs(sr, sc)
        
        return image
