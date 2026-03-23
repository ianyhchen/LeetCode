# Counting Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count, white_count, blue_count = 0, 0, 0

        for i in nums:
            if i == 0:
                red_count += 1
            elif i == 1:
                white_count += 1
            else:
                blue_count += 1
        
        for i in range(len(nums)):
            if red_count > 0:
                nums[i] = 0
                red_count -= 1
                continue
            elif white_count > 0:
                nums[i] = 1
                white_count -= 1
                continue
            else:
                nums[i] = 2
                blue_count -= 1

'''
荷蘭國旗算法 (One-pass) - 一次遍歷
思路：利用三個指針。
    - 當 curr 指向 0 時，與 p0 交換並讓 p0 和 curr 右移；
    - 當 curr 指向 2 時，與 p2 交換並讓 p2 左移（此時 curr 不動，因為交換過來的值還沒檢查）；
    - 當 curr 指向 1 時，直接跳過。
- 優點：只需遍歷一次，時間複雜度 O(n)，空間複雜度 O(1)。
- 效率比較：方法二比方法一更符合面試官對「最佳化」的期待。
'''    
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3-way Partitioning

        curr, p0, p2 = 0, 0, len(nums) - 1

        # The loop must include curr == p2 to ensure the element at p2 is processed
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                # After swapping with p2, we don't increment curr because 
                # the new element at curr needs to be inspected.
                p2 -= 1
            else: # nums[curr] == 1
                curr += 1    