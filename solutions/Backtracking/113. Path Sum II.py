# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []

        def dfs(node, current_path, remaining_sum):
            if not node:
                return

            # Add current node value to path
            current_path.append(node.val)

            # Check if it's a leaf node and the sum matches
            if not node.left and not node.right and node.val == remaining_sum:
                # Must append a copy of current_path
                res.append(list(current_path))
            else:
                # Recurse to children with updated remaining sum
                dfs(node.left, current_path, remaining_sum - node.val)
                dfs(node.right, current_path, remaining_sum - node.val)
            
            # Backtrack: remove the current node before going back up
            current_path.pop()
        
        dfs(root, [], targetSum)

        return res