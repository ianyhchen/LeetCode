# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        count = 0
        
        # Initialize counter and prefix sum map
        # sum_map stores {prefix_sum : count}
        sum_map = defaultdict(int)

        # Base case: a prefix sum of 0 happens once (before starting)
        # This handles paths that sum to targetSum starting from the root
        # 允許路徑從頭開始
        sum_map[0] = 1

        def dfs(node, curr_sum, sum_map):
            nonlocal count
            if not node:
                return
            
            # 1. Update the current prefix sum
            curr_sum += node.val

            # 2. Check if a valid sub-path exists ending at the current node
            # Formula: curr_sum - old_prefix_sum = targetSum 
            # => old_prefix_sum = curr_sum - targetSum
            prev_sum = curr_sum - targetSum
            if prev_sum in sum_map:
                count += sum_map[prev_sum]            
            
            # 3. Add the current prefix sum to the map for child nodes
            sum_map[curr_sum] += 1

            # 4. Recursively explore left and right children
            dfs(node.left, curr_sum, sum_map)            
            dfs(node.right, curr_sum, sum_map)

            # 5. Backtracking: Remove current sum from map before moving back up
            # This prevents this node's sum from affecting unrelated branches
            sum_map[curr_sum] -= 1
        
        dfs(root, 0, sum_map)

        return count
            
