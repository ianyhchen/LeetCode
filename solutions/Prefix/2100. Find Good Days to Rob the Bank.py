class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)

        # Base case: if time is 0, every day is a good day
        if time == 0:            
            return [i for i in range(n)]

        # 如果陣列長度根本不夠塞滿左右各 time 天，直接回傳空清單
        if n < 2 * time + 1:
            return []

        # left[i]: store the count of continuous non-increasing days before and including day i
        # right[i]: store the count of continuous non-decreasing days after and including day i
        left = [0] * n
        right = [0] * n

        # Pass 1: Scan from left to right to calculate non-increasing streaks
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1            

        # Pass 2: Scan from right to left to calculate non-decreasing streaks
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
                
        # Pass 3: Collect all valid days that satisfy the conditions on both sides
        result = []
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                result.append(i)

        return result