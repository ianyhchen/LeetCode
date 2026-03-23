class Solution:
    def __init__(self):
        self.res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sorting helps in pruning the search tree later
        candidates.sort()
        self.res = [] # Reset for multiple test cases if needed
        combination = []
        self.dfs(candidates, target, 0, 0, combination)
        return self.res
        
    def dfs(self, candidates: List[int], target: int, index: int, current_sum: int, comb: List[int]):
        if current_sum == target:
            # CRITICAL: Must use copy of comb because lists are mutable
            self.res.append(list(comb))
            return
        
        for i in range(index, len(candidates)):
            # Pruning: if adding this number exceeds target, 
            # no need to check current and subsequent numbers (since sorted)
            if current_sum + candidates[i] > target:
                break

            comb.append(candidates[i])
            # Pass 'i' instead of 'i+1' to allow reusing the same element
            self.dfs(candidates, target, i, current_sum + candidates[i], comb)
            # Backtrack: remove the last element before next iteration
            comb.pop()

