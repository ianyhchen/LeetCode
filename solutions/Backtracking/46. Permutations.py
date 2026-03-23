class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        res = []
        usedList = [False] * len(nums)

        def backTrack(permutation):
            if len(permutation) == len(nums):               
                res.append(list(permutation))
                return

            for i in range(len(nums)):
                if usedList[i]:
                    continue

                # Standard Backtracking steps
                permutation.append(nums[i])
                usedList[i] = True

                backTrack(permutation)

                # Restore state (Backtrack)
                permutation.pop()
                usedList[i] = False
        
        backTrack([])
        return res
