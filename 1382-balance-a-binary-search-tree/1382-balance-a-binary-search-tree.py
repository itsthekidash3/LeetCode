# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Goal:
        Take an existing (possibly skewed) BST and return a height-balanced BST
        containing the SAME node values.

        High-level idea:
        1. Inorder traversal of BST gives sorted values.
        2. Build a balanced BST from the sorted list using divide & conquer.
        """

        # Step 1: Store inorder traversal (sorted values)
        visited = []

        def inorder(node):
            """
            Inorder traversal of a BST yields values in sorted order.
            This ignores structure and only preserves value ordering.
            """
            if node is None:
                return
            
            inorder(node.left)
            visited.append(node.val)
            inorder(node.right)
        
        inorder(root)

        # Step 2: Build a balanced BST from the sorted array
        def constructTree(left, right):
            """
            Recursively construct a balanced BST from visited[left:right].

            - Pick the middle element as root (keeps tree height minimal)
            - Left half becomes left subtree
            - Right half becomes right subtree
            """
            if left > right:
                return None
            
            # Choose middle element to ensure balance
            mid = (left + right) // 2
            
            # Recursively build left and right subtrees
            leftNode = constructTree(left, mid - 1)
            rightNode = constructTree(mid + 1, right)

            # Create and return current root
            return TreeNode(visited[mid], leftNode, rightNode)
        
        # Construct balanced BST from full inorder list
        return constructTree(0, len(visited) - 1)
