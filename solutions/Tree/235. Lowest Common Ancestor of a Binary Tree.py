# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
DFS post order traversal

由於無法預知 p, q 的位置，我們定義一個遞迴函數 dfs(node)，它的傳回值定義如下：
- 如果 node 是空值，回傳 None。
- 如果 node 就是 p 或 q，回傳 node 本身。
- 關鍵邏輯：向左右子樹索取答案（left_res 和 right_res）：
    - 兩邊都有值：如果左邊回傳了一個節點，右邊也回傳了一個節點，代表 p 和 q 分佈在當前 node 的兩側 -> 當前的 node 就是 LCA。
    - 只有一邊有值：代表 p 和 q 都在同一側（或者只找到了其中一個），我們將那個「非空的值」繼續向上傳遞。
    - 兩邊都沒值：代表這棵子樹裡完全沒有 p 或 q。

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, node, p, q):
        # Base Case 1: Reach the end of a branch
        if not node:
            return None

        # Base Case 2: Found one of the targets
        if node == p or node == q:
            return node
        
        # Recursive step: Look for p and q in subtrees
        left_res = self.dfs(node.left, p, q)
        right_res = self.dfs(node.right, p, q)

        # 1. If both sides returned a node, current node is the LCA
        if left_res and right_res:
            return node

        # 2. If only one side has a value, propagate that value upwards
        # 3. If both are None, this returns None
        return left_res or right_res
