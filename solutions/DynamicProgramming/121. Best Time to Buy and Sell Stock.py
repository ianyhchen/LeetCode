class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        max_profit = 0

        for price in prices:
            # 1. 隨時更新歷史最低價            
            lowest_price = min(lowest_price, price)
            # 2. 隨時更新歷史最高利潤
            max_profit = max(max_profit, price - lowest_price)
        # 由於 max_profit 初始值為 0，且不可能為負，直接回傳即可
        return max_profit