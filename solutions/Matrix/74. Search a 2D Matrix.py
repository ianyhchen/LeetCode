# 將矩陣視為長度為 m * n 的有序陣列，直接進行一次二分搜尋
# Time complexity: O(log(m * n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, (m * n) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // n][mid % n]
            if target > mid_val:
                left = mid + 1
            elif target < mid_val:
                right = mid - 1
            else:
                return True
        
        return False