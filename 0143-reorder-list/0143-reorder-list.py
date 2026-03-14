# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # STRATEGY: Three-step process
        # 1. Find the middle of the list (slow/fast pointers)
        # 2. Reverse the second half
        # 3. Merge the two halves by alternating nodes
        
        # STEP 1: Find middle using slow/fast pointers
        # slow moves 1 step, fast moves 2 steps
        # When fast reaches end, slow is at the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2: Reverse the second half
        # Split list: slow is end of first half, slow.next is start of second half
        second = slow.next
        prev = slow.next = None  # Cut the list in half AND initialize prev for reversal
        
        # Standard linked list reversal
        while second:
            tmp = second.next       # Save next node
            second.next = prev      # Reverse the pointer
            prev = second           # Move prev forward
            second = tmp            # Move to next node
        # After loop, prev points to the new head of reversed second half
        
        # STEP 3: Merge two halves by alternating nodes
        # Pattern: first1 -> second1 -> first2 -> second2 -> ...
        first, second = head, prev
        while second:  # Second half might be shorter, so check it
            tmp1, tmp2 = first.next, second.next  # Save next pointers
            first.next = second    # Link first to second
            second.next = tmp1     # Link second to original first.next
            first, second = tmp1, tmp2  # Move both pointers forward
        
        # No return needed - we modified the list in-place!