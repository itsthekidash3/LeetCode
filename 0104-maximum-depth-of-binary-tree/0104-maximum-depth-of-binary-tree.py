# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ========== RECURSIVE DFS (MAIN SOLUTION) ==========
        # Base case: empty tree has depth 0
        if not root:
            return 0
        
        # Recursive case: 1 (current level) + max depth of left/right subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    # ========== BFS (LEVEL-ORDER TRAVERSAL) - COMMENTED OUT ==========
    # def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
    #     # Base case: empty tree
    #     if not root:
    #         return 0
    #     
    #     # Queue for level-order traversal
    #     q = deque()
    #     q.append(root)
    #     depth = 0
    #     
    #     # Process nodes level by level
    #     while q:  # While queue is not empty
    #         depth += 1  # Increment depth for each level
    #         
    #         # Process all nodes at current level
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             
    #             # Add children to queue for next level
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #     
    #     return depth


    # ========== ITERATIVE DFS (STACK-BASED) - COMMENTED OUT ==========
    # def maxDepth_iterative_dfs(self, root: Optional[TreeNode]) -> int:
    #     # Stack stores [node, depth] pairs
    #     stack = [[root, 1]]
    #     res = 0
    #     
    #     # Process nodes using stack (DFS)
    #     while stack:
    #         node, depth = stack.pop()
    #         
    #         if node:  # Only process non-null nodes
    #             res = max(res, depth)  # Update max depth seen
    #             
    #             # Add children with incremented depth
    #             stack.append([node.left, depth + 1])
    #             stack.append([node.right, depth + 1])
    #     
    #     return res