class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []        

        res = []
        # Set boundary
        top, bottom = 0, len(matrix) - 1, 
        left, right = 0,  len(matrix[0]) - 1 

        while top <= bottom and left <= right:
            # left -> right, fixed top
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # top -> bottom, fixed right
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # --- Critical Check Point ---
            # right -> left, fixed bottom
            # Since top already add one, we need to check top <= bottom
            if top <= bottom:
                for c in range(right, left - 1, -1):
                        res.append(matrix[bottom][c])
                bottom -= 1

            # bottom -> top, fixed left
            # Since right already minus 1, we need to check left <= right
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res