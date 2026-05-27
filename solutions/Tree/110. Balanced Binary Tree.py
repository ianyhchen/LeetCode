# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
One time pass DFS, 
time complexity: O(n)
Space complexity: O(n) in worse case,  O(log n) if balanced

自底向上（Bottom-up）思路：我們利用後序遍歷（左、右、中）的概念。從最底層的葉子節點開始往上回傳高度。重點：在回傳高度的過程中，如果發現某個子樹已經「不平衡」了，就直接回傳一個特殊值（例如 -1），表示這棵樹已經壞了，不需要再繼續計算。
優點：每個節點只會被訪問一次。時間複雜度為 O(n)
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1           

    def checkHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1

        diff = leftHeight - rightHeight
        if abs(diff) > 1:
            return -1
        
        #return height if balanced
        return max(leftHeight, rightHeight) + 1

        