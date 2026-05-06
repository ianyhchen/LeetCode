# 尋找長度為 `k` 的區間之「左邊界索引值」
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize the search range for the left boundary
        # The leftmost possible index is 0, the rightmost is n - k
        low = 0
        high = len(arr) - k

        # Standard Binary Search structure
        while low < high:
            mid = (low + high) // 2

            # Compare the distance of x with the element at 'mid' 
            # and the element at 'mid + k'
            # If x is closer to arr[mid + k] than to arr[mid],
            # it means the optimal window starts further to the right.
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                # Otherwise, the optimal window starts at mid or to the left
                high = mid

        # After the loop, 'low' is the starting index of the k closest elements
        return arr[low : low + k]