class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check 4 possible rotations (0, 90, 180, 270 degrees)
        for _ in range(4):
            # 1. Check if current matrix matches target
            if mat == target:
                return True
                
            # 2. Rotate the matrix 90 degrees clockwise
            self.rotate(mat)
        
        return False



    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the matrix 90 degrees clockwise in-place.
        Step 1: Transpose (Swap mat[i][j] with mat[j][i])
        Step 2: Reflect (Reverse each row)
        """
        n = len(matrix)

        # Step 1: Transpose
        # Only iterate through the upper triangle to avoid swapping back
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reflect (Reverse each row)
        for i in range(n):
            matrix[i].reverse()
                