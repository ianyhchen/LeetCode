'''
BFS solution
1. 將根節點放入 Queue 中。

2. 當 Queue 不為空時，執行循環：

    - 獲取目前 Queue 的長度 n（這代表目前這一層有多少個節點）。

    - 連續從 Queue 中取出 n 個節點，將它們的值存入一個暫時的 level_list。

    - 每取出一個節點，就將它的左右子節點（如果存在）再放入 Queue。

3. 將 level_list 加入最終結果。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if not root:
            return res
        else:
            queue.append(root)
        
        while queue:
            level_len = len(queue)
            level_list = []
            for _ in range(level_len):
                node = queue.popleft()
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_list)
        
        return res
            

