class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        index = 0
        n = len(intervals)

        if n == 0:
            return newInterval
        
        # 1. 處理新區間左側完全不重疊的區間
        # 條件：當前區間的結束時間 < 新區間的開始時間
        while index < n and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        # 2. 處理重疊部分，合併成一個大的新區間
        # 條件：當前區間的開始時間 <= 新區間的結束時間 (只要有交集就合併)
        # 不斷「吃掉」有重疊的部分，擴張 newInterval 的疆界
        while index < n and intervals[index][0] <= newInterval[1]:
            # 更新新區間的範圍：取兩者最小的起始值與最大的結束值
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1
        # add the merged new interval
        result.append(newInterval)

        # 3. 處理新區間右側完全不重疊的區間
        # 剩餘的區間直接加入
        while index < n:
            result.append(intervals[index])
            index += 1

        return result 