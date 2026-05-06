# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Initialize queue with (node, index)
        queue = deque()
        queue.append((root, 0))
        max_width = 0
        while queue:
            # Calculate width of the current level
            # queue[0] is the leftmost node, queue[-1] is the rightmost
            level_size = len(queue)
            current_level_width = queue[-1][1] - queue[0][1] + 1 
            max_width = max(max_width, current_level_width)

            # Process all nodes in the current level
            for _ in range(level_size):
                node, index = queue.popleft()

                # Assign 2*i for left child and 2*i+1 for right child
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return max_width