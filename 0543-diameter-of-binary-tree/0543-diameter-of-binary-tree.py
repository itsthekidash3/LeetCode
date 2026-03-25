# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Goal: Find the longest path between any two nodes (diameter)
        # Key insight: Diameter at a node = left height + right height
        # Use DFS to compute heights while tracking max diameter globally
        
        # Global variable to track maximum diameter found (use list for mutability)
        res = [0]

        def dfs(root):
            # Base case: empty node has height -1 (so leaf children contribute 0 edges)
            if not root:
                return -1
            
            # Recursively get height of left subtree
            left = dfs(root.left)
            
            # Recursively get height of right subtree
            right = dfs(root.right)
            
            # Update global max diameter
            # Diameter through current node = edges to left + edges to right
            # left and right are heights (-1 for null), so we add 2 to get edge count
            res[0] = max(res[0], 2 + left + right)
            
            # Return height of current node (1 edge to parent + max child height)
            return 1 + max(left, right)
        
        # Start DFS from root
        dfs(root)
        
        # Return the maximum diameter found
        return res[0]