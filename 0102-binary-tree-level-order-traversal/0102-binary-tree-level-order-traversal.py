# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Goal: Return level-order traversal (nodes grouped by depth/level)
        # Approach: BFS using queue - process one level at a time
        
        res = []  # Result: list of lists, each inner list is one level
        q = collections.deque()
        q.append(root)
        
        # Process nodes level by level while queue is not empty
        while q:
            qLen = len(q)  # Number of nodes at current level
            level = []  # Store values for current level
            
            # Process all nodes at current level
            for i in range(qLen):
                node = q.popleft()  # FIFO: get next node in level
                
                if node:  # Edge case: skip null nodes
                    level.append(node.val)  # Add value to current level
                    q.append(node.left)  # Add left child for next level
                    q.append(node.right)  # Add right child for next level
            
            # Only add non-empty levels to result
            if level:
                res.append(level)
        
        return res