# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of a linked list in one pass.
        
        Strategy: Two-pointer technique with n-node gap
        - Use dummy node to handle edge case (removing head)
        - Create n-node gap between right and left pointers
        - Move both together until right hits end
        - Left will be at node BEFORE the target → skip target node
        """
        
        # Dummy node prevents special-casing when removing the head
        # If we remove 1st node, dummy.next will point to the new head
        dummy = ListNode(0, head)
        
        left = dummy   # Will end up at node BEFORE nth-from-end
        right = head   # Used to measure the n-node gap
        
        # Phase 1: Create n-node gap between right and left
        # After this loop, right is n steps ahead of left
        for _ in range(n):
            right = right.next  # Note: should be right.next, not head.next
        
        # Phase 2: Move both pointers until right reaches the end
        # When right is None, left is at the node BEFORE our target
        while right:
            right = right.next  # Note: should be right.next, not head.next
            left = left.next    # Note: should be left.next, not dummy.next
        
        # Skip the nth node from end (left.next is the target)
        left.next = left.next.next
        
        # Return new head (handles case where original head was removed)
        return dummy.next