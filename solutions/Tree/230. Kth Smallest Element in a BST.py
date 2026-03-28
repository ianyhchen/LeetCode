# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        # Keep traversing if there are nodes to visit or nodes in the stack to backtrack to
        while curr or stack:
            # Phase 1: Go as deep as possible to the left
            while curr:
                stack.append(curr)
                curr = curr.left

            # Phase 2: Visit the node (Pop from stack)
            curr = stack.pop()

            # Decrement k and check if this is the target element
            k -= 1
            if k == 0:
                return curr.val
                
            # Phase 3: Move to the right child to explore its subtree
            curr = curr.right




    