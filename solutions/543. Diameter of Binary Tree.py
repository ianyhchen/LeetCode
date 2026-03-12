# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            # 遞迴終止條件：如果節點為空，高度為 0
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal res
            # 更新最大直徑：左高度 + 右高度
            # 這代表經過當前節點的最長路徑（邊數）
            res = max(res, l + r) 
            
            # 回傳當前節點的高度給父節點
            # 挑選左右較長的那一邊，並加上連往父節點的那條邊 (+1)
            return 1 + max(l, r)

        dfs(root)        
        return res