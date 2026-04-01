# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Goal: Reconstruct binary tree from preorder and inorder traversals
        # Key insights:
        # 1. Preorder: first element is always the root (root → left → right)
        # 2. Inorder: elements left of root are left subtree, right are right subtree (left → root → right)
        
        # Base case: empty list means no tree/subtree
        if not preorder or not inorder:
            return None
        
        # Step 1: First element in preorder is the root
        root = TreeNode(preorder[0])
        
        # Step 2: Find root's position in inorder to split left/right subtrees
        mid = inorder.index(preorder[0])
        
        # Step 3: Recursively build left subtree
        # Preorder: skip root (index 0), take next 'mid' elements (left subtree size)
        # Inorder: take everything before mid (left of root)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Step 4: Recursively build right subtree
        # Preorder: skip root and left subtree elements (start at mid+1)
        # Inorder: take everything after mid (right of root)
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root