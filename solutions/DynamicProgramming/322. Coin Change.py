class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:    
        # 1. Initialize DP table with amount + 1 (an impossible max value)
        # Size is amount + 1 to include index 'amount'
        dp = [float('inf')] * (amount + 1)

        # 2. Base case: 0 coins needed to make amount 0
        dp[0] = 0

        # 3. Iterate through every amount from 1 to 'amount'
        for value in range(1, amount + 1):
            for coin in coins:
                if value - coin >= 0:
                    # Update the minimum coins needed for current amount 'value'
                    dp[value] = min(dp[value], dp[value - coin] + 1)
                    
        # 4. If dp[amount] is still inf, it means the amount cannot be reached
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]

