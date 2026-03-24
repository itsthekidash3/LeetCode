# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Goal: Mirror the binary tree (swap left and right subtrees at every node)
        # Approach: DFS recursion - swap children, then recursively invert subtrees
        
        # Base case: empty tree returns None
        if not root:
            return None
        
        # Swap the left and right children of current node
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # Recursively invert the left subtree (now on the right after swap)
        self.invertTree(root.left)
        
        # Recursively invert the right subtree (now on the left after swap)
        self.invertTree(root.right)
        
        # Return the root of the inverted tree
        return root