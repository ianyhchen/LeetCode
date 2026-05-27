'''
1. 預留標記位：使用兩個布林變數獨立記錄「原始第一行」與「原始第一列」是否包含 0。

2. 內部標記：遍歷其餘區域 matrix[1:][1:]，若發現 0，則在對應的第一行與第一列位置打上 0 作為標記。

3. 根據標記更新：依據第一行與第一列的標記值，將內部的元素設為 0。

4. 最後處理首行首列：根據步驟 1 的布林變數，決定是否將整條首行或首列設為 0。
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero, first_col_zero = False, False

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # Set the first cell of current row and col as 0
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):            
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0