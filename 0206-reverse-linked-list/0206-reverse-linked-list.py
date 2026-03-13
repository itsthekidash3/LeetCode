# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach: O(n) time, O(1) space
        # Use three pointers to reverse links in-place
        
        prev = None  # Will become the new tail (originally null)
        curr = head  # Start at the head, will traverse the entire list
        
        while curr:
            nxt = curr.next          # Save next node before breaking the link
            curr.next = prev         # Reverse the pointer to point backwards
            prev = curr              # Move prev forward to current node
            curr = nxt               # Move curr forward to next node
        
        return prev  # prev is now the new head (last node visited)


    # Recursive Approach: O(n) time, O(n) space (call stack)
    # Recursively reach the end, then reverse pointers on the way back up
    
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # Base cases: empty list or single node
    #     if not head or not head.next:
    #         return head
    #     
    #     # Recursively reverse the rest of the list
    #     newHead = self.reverseList(head.next)
    #     
    #     # Reverse the link: make the next node point back to current
    #     head.next.next = head
    #     
    #     # Set current node's next to None (will be updated by previous call or remain as tail)
    #     head.next = None
    #     
    #     return newHead  # Pass the new head back up through all recursive calls