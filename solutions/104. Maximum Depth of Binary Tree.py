# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxHeight(root)
    #dfs 遞迴找左右子樹高度，每個節點的最大深度為左右子樹最大高度 + 1    
    def getMaxHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        leftHeight = self.getMaxHeight(node.left)
        rightHeight = self.getMaxHeight(node.right)

        return max(leftHeight, rightHeight) + 1