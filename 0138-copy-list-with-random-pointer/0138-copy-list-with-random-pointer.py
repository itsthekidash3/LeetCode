"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Deep copy a linked list where each node has a random pointer.
        
        Strategy: Two-pass with hashmap
        Pass 1: Create all new nodes, map old→new
        Pass 2: Wire up next and random pointers using the map
        
        Why hashmap? Random pointers can point to ANY node (even forward),
        so we need all nodes created before we can wire them up.
        """
        
        # Map old nodes to their copies
        # {None: None} handles edge case: when curr.next or curr.random is None
        oldToNew = {None: None}
        
        # PASS 1: Create all new nodes (just values, no connections yet)
        curr = head
        while curr:
            copy = Node(curr.val)  # Clone the value only
            oldToNew[curr] = copy  # Map: original node → copy node
            curr = curr.next       # Traverse original list
        
        # PASS 2: Wire up the pointers in the copied list
        curr = head
        while curr:
            copy = oldToNew[curr]              # Get the copy of current node
            copy.next = oldToNew[curr.next]    # Connect next (via map lookup)
            copy.random = oldToNew[curr.random] # Connect random (via map lookup)
            curr = curr.next                    # Traverse original list
        
        # Return the head of the copied list
        # (head could be None, that's why we added None:None to map)
        return oldToNew[head]