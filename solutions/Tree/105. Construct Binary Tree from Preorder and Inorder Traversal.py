# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use python slicing
# Time & space complexity: O(n**2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # 1. 確定根節點
        root = TreeNode(preorder[0])

        # 2. 在中序遍歷中找到根節點位置，以此區分左右子樹
        # 這裡隱含了一個 O(N) 的搜尋操作
        mid = inorder.index(preorder[0])

        # 3. 遞迴構建左右子樹
        # preorder[1:mid+1]：前序中，根之後的 mid 個元素是左子樹
        # inorder[:mid]：中序中，根之前的元素是左子樹
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])

        # preorder[mid+1:]：前序中，剩下的部分是右子樹
        # inorder[mid+1:]：中序中，根之後的元素是右子樹
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
    


# 4 pointer
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a hashmap to store the value -> index mapping for inorder traversal
        # This allows O(1) lookup to find the root's position
        inorder_index_map = {val:i for i, val in enumerate(inorder)}

        # Helper function to build the tree using pointers to avoid list slicing
        def array_to_tree(pre_left, pre_right, in_left, in_right):
            # Base case: if there are no elements to construct the tree
            if pre_left > pre_right:
                return None
            # The first element in preorder is always the root of the current subtree
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Find the index of this root in the inorder list
            root_index_in_inorder = inorder_index_map[root_val]

            # Number of nodes in the left subtree
            # * Note: 需要多想想 *
            left_subtree_size = root_index_in_inorder - in_left

            # Recursively build the left subtree
            # Preorder range for left: [pre_left + 1, pre_left + left_subtree_size]
            # Inorder range for left: [in_left, root_index_in_inorder - 1]
            root.left = array_to_tree(pre_left + 1, pre_left + left_subtree_size, in_left, root_index_in_inorder - 1)

            # Recursively build the right subtree
            # Preorder range for right: [pre_left + left_subtree_size + 1, pre_right]
            # Inorder range for right: [root_index_in_inorder + 1, in_right]
            root.right = array_to_tree(pre_left + left_subtree_size + 1, pre_right, root_index_in_inorder + 1, in_right)            
            
            return root
        
        return array_to_tree(0, len(preorder) - 1, 0, len(inorder) - 1)
