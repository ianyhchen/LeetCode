# DFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Boundary condition: if the tree is empty, no path exists.
        if not root:
            return False        

        def dfs(node, remaining_sum):
            # Base case: if we hit a null child, this path is invalid.        
            if not node:
                return False

            # Success condition: check if the current node is a leaf 
            # and its value matches the remaining sum.
            if not node.left and not node.right and remaining_sum == node.val:
                return True            

            # Recursive step: subtract current node's value from remaining_sum
            # and search in both left and right subtrees.
            # Return True if either subtree contains a valid path.
            return dfs(node.left, remaining_sum - node.val) or dfs(node.right, remaining_sum - node.val)

        return dfs(root, targetSum)