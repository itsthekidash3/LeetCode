"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Goal: Create deep copy of undirected graph
        # Challenge: Nodes reference each other (circular dependencies)
        # Approach: DFS with hashmap to track old→new node mappings
        # Key insight: Map prevents infinite recursion and ensures same node isn't cloned twice
        
        # Map original nodes to their clones
        oldToNew = {}
        
        def dfs(node):
            # Base case 1: Node already cloned (prevents infinite recursion)
            if node in oldToNew:
                return oldToNew[node]  # Return existing clone
            
            # Step 1: Create clone with same value (empty neighbors for now)
            copy = Node(node.val)
            
            # Step 2: Store mapping BEFORE recursing (crucial for cycles!)
            oldToNew[node] = copy
            
            # Step 3: Clone all neighbors recursively
            for nei in node.neighbors:
                # dfs(nei) returns the cloned neighbor node
                # Append that clone to current node's neighbor list
                copy.neighbors.append(dfs(nei))
            
            # Step 4: Return completed clone
            return copy
        
        # Edge case: empty graph
        return dfs(node) if node else None