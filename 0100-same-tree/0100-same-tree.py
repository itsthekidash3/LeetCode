# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Goal: Check if two binary trees are structurally identical with same values
        # Approach: DFS recursion - compare current nodes, then recursively check subtrees
        
        # Base case: both trees are empty (same)
        if not p and not q:
            return True
        
        # Recursive case: both nodes exist and have same value
        if p and q and p.val == q.val:
            # Check if left subtrees match AND right subtrees match
            # Use 'self.' because isSameTree is a class method, not a standalone function
            # 'self' refers to the current Solution instance
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # All other cases: trees differ (one null, values mismatch, or structure differs)
        return False