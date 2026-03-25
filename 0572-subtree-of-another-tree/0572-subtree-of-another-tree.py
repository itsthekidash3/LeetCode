# everything is a sub problem. You just have to get habituated to breaking it down and focus!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Goal: Check if subRoot is a subtree of root (identical structure somewhere in root)
        # Approach: For each node in root, check if tree starting there matches subRoot
        
        # Edge case: empty subRoot is always a subtree (null is subset of everything)
        if not subRoot:
            return True
        
        # Edge case: empty root can't contain a non-empty subRoot
        if not root:
            return False
        
        # Check if current node's tree matches subRoot exactly
        if self.sameTree(root, subRoot):
            return True
        
        # Recursively check if subRoot exists in left OR right subtree
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def sameTree(self, s, t):
        # Helper: Check if two trees are identical (same structure and values)
        
        # Base case: both empty trees are identical
        if not s and not t:
            return True
        
        # Both nodes exist with same value - check subtrees recursively
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and 
                    self.sameTree(s.right, t.right))
        
        # Mismatch: one is null, values differ, or structure differs
        return False