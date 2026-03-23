# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            # If both p and q are greater than curr, the LCA must be in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are smaller than curr, the LCA must be in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # We found the split point (one is on the left, one on the right) 
                # or curr is equal to p or q. In either case, curr is the LCA.
                return curr
        