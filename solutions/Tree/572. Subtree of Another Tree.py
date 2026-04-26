# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        def isSameTree(s, t):
            # Both nodes are null, trees are identical up to this point
            if not s and not t:
                return True
            # One node is null or values differ, trees are not identical
            if not s or not t or s.val != t.val:
                return False

            # Recursively check both left and right subtrees
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # Base case: if main tree is empty, it can't contain any subRoot
        if not root:
            return False

        # If current root matches subRoot, return True
        if isSameTree(root, subRoot):        
            return True
            
        # Otherwise, search for subRoot in the left or right child
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

            