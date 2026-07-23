# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, curr_max):
            if not node:
                return 0 # 空節點貢獻 0

            # 1. 判斷自己是不是好節點
            is_good = 1 if node.val >= curr_max else 0
            
            # 更新這條路徑上的最大值
            curr_max = max(curr_max, node.val)

            # 2. 遞迴左右子樹，並把各自帶回來的數量加起來
            left_count = dfs(node.left, curr_max)
            right_count = dfs(node.right, curr_max)
            
            # 3. 匯總回傳給上一層
            return is_good + left_count + right_count
        
        return dfs(root, root.val)
            

            
            