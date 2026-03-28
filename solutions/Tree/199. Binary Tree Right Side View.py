# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []

        if not root:
            return res
        
        queue.append(root)
        
        while queue:
            level_num = len(queue)            
            for i in range(level_num):
                node = queue.popleft()

                # Since we push right child first, the 0-th element 
                # of each level is the rightmost node.
                if i == 0:
                    res.append(node.val)
                    
                # Push right first to keep it as the "head" of the level
                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
      
        return res
            
        