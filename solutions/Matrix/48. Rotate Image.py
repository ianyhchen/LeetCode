class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        

        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Transpose the matrix
        # We swap matrix[i][j] with matrix[j][i]
        for i in range(rows):
            # Start j from i to avoid swapping elements back to their original positions
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]        
        
        # Step 2: Reverse each row
        # This converts the transposed matrix into a 90-degree clockwise rotated matrix      
        for i in range(rows):
            # Use two pointers to reverse the elements in the current row in-place
            left, right = 0, cols - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
            
            # Slicing
            # matrix[i][:] = matrix[i][::-1] 

            # built-in function
            #matrix[i].reverse()
        
            
