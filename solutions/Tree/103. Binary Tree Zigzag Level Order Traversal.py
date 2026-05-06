# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Deque 雙端插入
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the queue for BFS and the result list
        queue = deque()
        res = []

        # Base case: if the tree is empty, return an empty list
        if not root:
            return res
        else:
            queue.append(root)

        # Flag to track the direction of traversal
        # True: Left to Right, False: Right to Left
        is_left_to_right = True
        while queue:
            level_len = len(queue)
            # Use a deque for the current level to allow efficient O(1) insertions at both ends
            level_list = deque()

            for _ in range(level_len):
                # Always pop from the left to maintain the standard BFS scan order (Left to Right)
                node = queue.popleft()

                # Based on the current direction, decide where to insert the node's value
                if is_left_to_right:
                    # Normal order: add to the end
                    level_list.append(node.val)
                else:
                    # Reverse order: add to the front
                    level_list.appendleft(node.val)

                # Always add children in Left-to-Right order to keep the BFS structure intact
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Convert the deque to a standard list before appending to the final results
            res.append(list(level_list))
            is_left_to_right = False if is_left_to_right else True

        return res

# 標準 BFS + 結果翻轉
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the queue for BFS and the result list
        queue = deque()
        res = []

        # Base case: if the tree is empty, return an empty list
        if not root:
            return res
        else:
            queue.append(root)

        # Flag to track the direction of traversal
        # True: Left to Right, False: Right to Left
        is_left_to_right = True
        while queue:
            level_len = len(queue)
            level_list = []

            for _ in range(level_len):
                # Always pop from the left to maintain the standard BFS scan order (Left to Right)
                node = queue.popleft()
                level_list.append(node.val)

                # Always add children in Left-to-Right order to keep the BFS structure intact
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # If the current level requires Right-to-Left order, reverse the list
            # This is an O(k) operation where k is the number of nodes in this level
            if not is_left_to_right:                
                level_list.reverse()

            res.append(level_list)
            is_left_to_right = False if is_left_to_right else True

        return res
