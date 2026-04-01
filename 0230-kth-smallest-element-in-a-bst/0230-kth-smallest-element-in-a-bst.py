# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def inorder(self, root, values):
        # Helper: Perform inorder traversal (left → root → right)
        # Inorder traversal of BST produces sorted values in ascending order
        
        # Base case: empty node
        if root is None:
            return 
        
        # Step 1: Traverse left subtree (smaller values)
        self.inorder(root.left, values)
        
        # Step 2: Process current node (add to list)
        values.append(root.val)
        
        # Step 3: Traverse right subtree (larger values)
        self.inorder(root.right, values)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Goal: Find the kth smallest element in a BST
        # Approach: Inorder traversal gives sorted order, return kth element
        # Key insight: Inorder of BST = sorted array
        
        values = []  # Store all values in sorted order
        self.inorder(root, values)  # Fill values using inorder traversal
        
        # Return kth smallest (k-1 because 0-indexed)
        return values[k - 1]


    # ========== ITERATIVE SOLUTION (OPTIMIZED - EARLY TERMINATION) ==========
    # def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
    #     # Goal: Find kth smallest without storing all values
    #     # Approach: Iterative inorder traversal, stop at kth node
    #     # Advantage: O(H + k) time, O(H) space vs O(N) for both in recursive
    #     
    #     n = 0  # Counter for nodes visited in sorted order
    #     stack = []  # Stack for iterative traversal
    #     cur = root
    #     
    #     # Iterative inorder traversal
    #     while cur or stack:  # Continue while nodes to process
    #         # Step 1: Go to leftmost node (smallest unvisited)
    #         while cur:
    #             stack.append(cur)  # Save path
    #             cur = cur.left
    #         
    #         # Step 2: Process node (this is next in sorted order)
    #         cur = stack.pop()
    #         n += 1  # Increment count of visited nodes
    #         
    #         # Step 3: Check if we've reached kth smallest
    #         if n == k:
    #             return cur.val
    #         
    #         # Step 4: Move to right subtree (larger values)
    #         cur = cur.right