from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp[i] = max(dp[i - 1], profit[i] + dp[last_not_conflict_job]

        # 1. Combine jobs and sort by ending time to enable DP progression
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x : x[1])
        n = len(jobs)

        # 2. Extract sorted end times for binary search efficiency
        end_times = [job[1] for job in jobs]

        # 3. Initialize DP array where dp[i] is max profit from first i jobs
        # dp[0] is 0 as a base case (no jobs selected)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curr_start, curr_end, curr_profit = jobs[i - 1]

            # 4. Find the last non-conflicting job index
            # bisect_right returns insertion point for curr_start
            # Subtract 1 to get the index of the job ending at or before curr_start
            prev_index = bisect_right(end_times, curr_start) - 1

            # 5. Transition: Max of (skipping current job) or (taking current + previous max)
            # dp[prev_index + 1] refers to the max profit up to the found non-conflicting job
            profit_if_taken = curr_profit + dp[prev_index + 1]            
            profit_if_not_taken = dp[i - 1]

            dp[i] = max(profit_if_not_taken, profit_if_taken)

        return dp[n]
