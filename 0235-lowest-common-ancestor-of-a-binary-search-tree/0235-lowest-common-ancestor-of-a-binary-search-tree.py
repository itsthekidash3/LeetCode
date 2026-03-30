# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Goal: Find the lowest common ancestor (LCA) of two nodes in a BST
        # Key insight: BST property means we can navigate without recursion
        # LCA is the split point where p and q diverge to different subtrees
        
        cur = root
        
        while cur:
            # Case 1: Both p and q are in the right subtree
            # (both values greater than current node)
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # Case 2: Both p and q are in the left subtree
            # (both values less than current node)
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # Case 3: Split point found - one goes left, one goes right
            # (OR one of them is the current node itself)
            # This is the LCA
            else:
                return cur