# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 將有向的樹 (Directed Tree) 轉化為無向圖 (Undirected Graph)
# 由於二元樹預設只能由上往下遍歷，因此第一步需先將其轉換為「無向圖」的概念。透過 DFS 紀錄每個節點的 Parent 後，再以 BFS 同時向「左、右、上」三個方向擴散
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        # Boundary case: if k is 0, the only node at distance 0 is target itself
        if k == 0 and target:
            return [target.val]

        parent_map = {}

        # DFS to map each node to its parent
        def findParent(node, p):
            if not node:
                return            
            
            parent_map[node] = p
            findParent(node.left, node)
            findParent(node.right, node)

        findParent(root, None)

        # BFS to find nodes at distance K        
        queue = deque()
        queue.append(target)
        visited = {target}  # CRITICAL: target must be marked as visited initially
        level = 0
        while queue:
            # We found the nodes at the current level which is distance K
            if level == k:
                return [node.val for node in queue]

            size = len(queue)
            for _ in range(size):
                curr_node = queue.popleft()

                # Check three directions: left, right, and parent
                for neighbor in (curr_node.left, curr_node.right, parent_map.get(curr_node)):                
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            level += 1                    
        
        return []