# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Goal: Count "good" nodes (nodes >= all values on path from root to itself)
        # Approach: DFS preorder traversal, track max value seen on current path
        
        def dfs(node, maxVal):
            # Base case: null node contributes 0 good nodes
            if not node:
                return 0
            
            # Check if current node is "good" (>= all ancestors on path)
            res = 1 if node.val >= maxVal else 0
            
            # Update max value for children's paths
            maxVal = max(maxVal, node.val)
            
            # Recursively count good nodes in left subtree
            res += dfs(node.left, maxVal)
            
            # Recursively count good nodes in right subtree
            res += dfs(node.right, maxVal)
            
            return res
        
        # Start DFS from root with root's value as initial max
        return dfs(root, root.val)