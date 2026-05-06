'''
- 前綴和 (Prefix Sum)：將權重轉化為連續的數值區間座標。
- 二分搜尋 (Binary Search)：在有序的前綴和陣列中，快速定位隨機數落在噴哪個區間。
'''
import random
class Solution:

    def __init__(self, w: List[int]):
        # Initialize the prefix sums list
        self.prefix_sums = []
        curr_sum = 0
        for i in w:
            curr_sum += i
            self.prefix_sums.append(curr_sum)

        # Total sum is the last element of prefix_sums
        self.total_sum = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        # Generate a random integer between 1 and total_sum (inclusive)        
        random_num = random.randint(1, self.total_sum)
        return self.binarySearch(random_num)

    def binarySearch(self, target) -> int:
        left, right = 0, len(self.prefix_sums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == self.prefix_sums[mid]:
                return mid
            elif target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        # When target is not found, 'left' will point to the first 
        # element that is greater than the target.
        return left

        
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()