# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS solution
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        def dfs(node):
            if node is None:
                nodes.append("null")
                return

            # Root -> Left -> Right (Preorder)
            nodes.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        res = ",".join(nodes)
        return res

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Use deque for O(1) popleft operations
        val_list = deque(data.split(','))

        def dfs(val_list):
            val = val_list.popleft()

            if val == 'null':
                return None
            # Create the current node
            node = TreeNode(int(val))
            # Recursively build left and right subtrees
            node.left = dfs(val_list)
            node.right = dfs(val_list)

            return node
        
        return dfs(val_list)


# BFS solution
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                # 1. 它是正常節點：記錄數值
                res.append(str(node.val))
                # 2. 將左右小孩放入 Queue (不管是 None 還是節點)
                queue.append(node.left)
                queue.append(node.right)        
            else:
                # 3. 它是 None：記錄 null，且不用再往 Queue 塞小孩
                res.append("null")
        
        return ",".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # Use deque for O(1) popleft operations
        val_list = data.split(',')
        queue = deque()
        
        root = TreeNode(int(val_list[0]))
        queue.append(root)
        i = 1 # 指標，從第二個元素開始發放
        # 發放小孩: 每從 Queue 出來一個節點，它就必須從字串清單中領走接下來的兩個位置
        while queue and i < len(val_list):
            parent = queue.popleft()

            # --- 處理左小孩 ---
            if val_list[i] != "null":
                parent.left = TreeNode(int(val_list[i]))
                queue.append(parent.left) # 它是活的，以後也要當父母
            i += 1 # 指標往後移

            # --- 處理右小孩 ---
            # 注意：要檢查 i 是否越界 (雖然序列化正確時不會發生)
            if i < len(val_list) and val_list[i] != "null":
                parent.right = TreeNode(val_list[i])
                queue.append(parent.right)
            i += 1        
        
        return root