# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Goal: Validate if tree follows BST property (left < node < right for all nodes)
        # Approach: DFS with valid range boundaries for each subtree
        # Key insight: Each node must be within a valid range inherited from ancestors
        
        def isValid(node, leftB, rightB):
            # Base case: empty tree is a valid BST
            if not node:
                return True
            
            # Check if current node violates BST property
            # Node must be strictly between leftB (exclusive) and rightB (exclusive)
            if not (node.val > leftB and node.val < rightB):
                return False
            
            # Recursively validate left and right subtrees with updated boundaries
            # Left subtree: all values must be < node.val (update right boundary)
            # Right subtree: all values must be > node.val (update left boundary)
            return (isValid(node.left, leftB, node.val) and
                    isValid(node.right, node.val, rightB))
        
        # Start validation with infinite boundaries (any value initially valid)
        return isValid(root, float("-inf"), float("inf"))