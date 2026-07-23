class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. Sort the candidates to handle duplicates and enable early pruning
        candidates.sort()
        res = []
           
        def dfs(index: int, current_sum: int, comb:List[int]):
            # Base Case 1: We found a valid combination
            if current_sum == target:
                res.append(list(comb)) # Append a copy of the current path
                return
            
            # Base Case 2: The sum exceeds target (Pruning)
            # Since candidates are sorted, any subsequent element will also be too large
            if current_sum > target:
                return

            for i in range(index, len(candidates)):
                # 2. Skip duplicates to prevent duplicate combinations (Sibling/Horizontal Pruning)
                # 'i > index' ensures we only skip when we are at the same recursion depth (horizontal)
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if current_sum + candidates[i] > target:
                    break

                # 3. Choose the current number
                comb.append(candidates[i])

                # 4. Explore (Vertical recursion)
                # Move to the next index 'i + 1' since each number can only be used once
                dfs(i + 1, current_sum + candidates[i], comb)
                
                # 5. Backtrack (Undo choice)
                comb.pop()
        
        dfs(0, 0, [])
        return res

