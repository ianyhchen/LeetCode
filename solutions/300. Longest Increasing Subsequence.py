# DP, O(n ** 2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Initialize DP array where each element is 1 
        # (each number is a subsequence of length 1)
        dp = [1] * len(nums)

        # Iterate through each element in the array
        for i in range(1, len(nums)):
            # Check all elements before the current element i
            for j in range(i):
                # If current element is greater than the previous element,
                # it can form an increasing subsequence
                if nums[i] > nums[j]: 
                    # Update dp[i] with the maximum length found so far
                    dp[i] = max(dp[i], dp[j] + 1)
        # The answer is the maximum value in the dp array
        return max(dp)