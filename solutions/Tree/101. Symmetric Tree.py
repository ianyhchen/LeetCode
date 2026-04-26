# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Base case: an empty tree is symmetric
        if not root:
            return True

        # Initialize deque with the left and right children of root as a pair
        # We store them as a tuple (L, R) in the queue
        queue = deque([(root.left, root.right)])

        while queue:
            # Extract the pair that should be symmetric
            L, R = queue.popleft()

            # If both are None, they are symmetric; move to the next pair
            if not L and not R:
                continue
            # If one is None or values don't match, it's not symmetric
            if not L or not R or L.val != R.val:
                return False  

            # Add next pairs in "mirror order":
            # 1. Left child's left with Right child's right (Outer)
            queue.append((L.left, R.right))
            # 2. Left child's right with Right child's left (Inner)
            queue.append((L.right, R.left))
        
        return True

# DFS

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
        
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left) 
        
        return isMirror(root.left, root.right)
