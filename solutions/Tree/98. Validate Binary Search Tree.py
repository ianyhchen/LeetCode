'''
根據 BST 的定義，有效的 BST 必須滿足以下三個條件：

1. 節點的 左子樹 只包含 小於 當前節點值的節點。

2. 節點的 右子樹 只包含 大於 當前節點值的節點。

3. 所有左子樹與右子樹本身也必須是二元搜尋樹。


常見錯誤:

1. 局部檢查陷阱：只檢查 node.val > node.left.val 和 node.val < node.right.val。這是不夠的！例如，右子樹中可能隱藏一個比根節點還小的節點，這會違反 BST 定義。

2. 邊界值處理：題目中節點的值範圍可能包含 Python 的整數極限，或是 C++/Java 的 INT_MIN / INT_MAX。如果使用方法一時，初始範圍設定不夠廣（例如設為 float('-inf') 以外的固定數值），可能會在邊界測資失敗。

3. 嚴格遞增：記得 BST 要求是「大於」或「小於」，相等的值也是不允許的（除非題目特別說明）。
'''
# DFS solution
#在遞迴時，攜帶兩個參數 low 和 high，代表當前節點值的合法範圍

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:     
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, node, low, high) -> bool:
        if node is None:
            return True
        
        if node.val <= low or node.val >= high:
            return False

        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)


# In-order Traversal solution
# BST 的一個重要性質是：中序走訪的結果必須是嚴格遞增的
# 用一個變數紀錄「前一個走訪到的節點值」。在遍歷過程中，只要當前值 <= 前一個值，就代表這不是有效的 BST
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:     
        self.prev = float('-inf') # 初始化為最小值
        return self.inorder(root)

    def inorder(self, node):
        if not node:
            return True
        
        # 往左走 (如果左邊失敗就回傳 False)
        if not self.inorder(node.left):
            return False

        # 檢查當前節點 (跟 self.prev 比較)
        # 如果違規回傳 False，否則更新 self.prev
        if node.val <= self.prev:
            return False        
        self.prev = node.val

        # 往右走
        return self.inorder(node.right)