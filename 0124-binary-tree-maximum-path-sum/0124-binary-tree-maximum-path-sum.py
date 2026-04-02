# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Goal: Find the maximum path sum in a binary tree (path = any node-to-node connection)
        # Approach: DFS to compute max path at each node, tracking global maximum
        # Key insight: At each node, consider two scenarios:
        #   1. Path that splits through this node (left → node → right)
        #   2. Path that continues through this node (node → one subtree)
        
        # Global variable to track maximum path sum found (use list for mutability)
        res = [root.val]

        # Helper: returns max path sum WITHOUT splitting at this node
        def dfs(root):
            # Base case: null node contributes 0 to path sum
            if not root:
                return 0
            
            # Recursively get max path sum from left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # Ignore negative paths (better to not include them)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Scenario 1: Compute max path WITH split at current node
            # (left subtree → current node → right subtree)
            # Update global maximum if this path is better
            res[0] = max(root.val + leftMax + rightMax, res[0])
            
            # Scenario 2: Return max path WITHOUT split for parent nodes
            # (current node can only extend one direction upward)
            # Choose the better subtree to extend from
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]