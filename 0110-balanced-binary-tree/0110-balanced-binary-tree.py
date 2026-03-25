# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function returns height if balanced, -1 if unbalanced
        def dfs(node):
            # Base case: empty tree has height 0 and is balanced
            if not node:
                return 0
            
            # Get height of left subtree (or -1 if unbalanced)
            left = dfs(node.left)
            if left == -1:  # Left subtree is unbalanced, propagate failure
                return -1
            
            # Get height of right subtree (or -1 if unbalanced)
            right = dfs(node.right)
            if right == -1:  # Right subtree is unbalanced, propagate failure
                return -1
            
            # Check if current node is balanced (height difference ≤ 1)
            if abs(left - right) > 1:
                return -1  # Current node unbalanced, mark as failure
            
            # Current node is balanced, return its height
            return 1 + max(left, right)
        
        # Tree is balanced if dfs doesn't return -1
        return dfs(root) != -1