# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the node is empty, return None
        if root is None:
            return None
        # Swap the left and right children using Python's tuple unpacking
        root.left, root.right = root.right, root.left

        # Recursively invert the left sub-tree
        self.invertTree(root.left)
        # Recursively invert the right sub-tree
        self.invertTree(root.right)

        return root