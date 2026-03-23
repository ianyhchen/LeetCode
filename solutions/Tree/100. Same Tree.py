# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS solution
# Time complexity is O(n), where 'n' is the number of nodes in the larger of the two trees.
# Space complexity is O(h), where 'h' is the height of the tree,
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both trees are empty, they are identical.
        if p is None and q is None:
            return True
        elif p is None or q is None: # If one of the trees is empty and the other is not, they are not identical.
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
    
    
'''
BFS solution
Time and space complexity  O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS solution
        queue_p = deque()
        queue_q = deque()

        queue_p.append(p)
        queue_q.append(q)

        while queue_p and queue_q:
            node1 = queue_p.popleft()
            node2 = queue_q.popleft()

            if not node1 and not node2:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            
            queue_p.append(node1.left)
            queue_p.append(node1.right)
            queue_q.append(node2.left)
            queue_q.append(node2.right)
        
        return not queue_p and not queue_q




        
    
    