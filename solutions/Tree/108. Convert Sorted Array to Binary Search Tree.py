# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Time Complexity: O(N)，每個數字都恰好被訪問並轉換成節點一次。
Space Complexity: O(log N)
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            # Base case: if the range is empty
            if left > right:
                return None

            # Always choose the left middle node as the root to maintain balance
            mid = left + (right - left) // 2

            # Create the current root node with the middle value
            root = TreeNode(nums[mid])

            # Recursively build the left subtree using the left half of the array
            root.left = helper(left, mid - 1)

            # Recursively build the right subtree using the right half of the array
            root.right = helper(mid + 1, right)

            # Return the current root to the caller (parent node)
            return root

        # Initiate the recursion with the full range of the array
        return helper(0, len(nums) - 1)
        
