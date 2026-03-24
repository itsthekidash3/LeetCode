# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node simplifies edge cases (reversing from the very first group)
        dummy = ListNode(0, head)
        groupPrev = dummy  # Pointer to the node BEFORE the current group
        
        while True:
            # Find the kth node in the current group (returns None if < k nodes left)
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # Not enough nodes left to form a group of k
            
            # Save the first node of the NEXT group (we'll reconnect to it later)
            groupNext = kth.next
            
            # Reverse the current group of k nodes
            # prev starts at groupNext (what the reversed group will point to)
            # curr starts at the first node of the current group
            prev, curr = kth.next, groupPrev.next
            
            # Standard iterative reversal - stop when we've processed k nodes
            while curr != groupNext:  # Loop until curr reaches the node AFTER kth
                tmp = curr.next       # Save next node before breaking the link
                curr.next = prev      # Reverse the pointer
                prev = curr           # Move prev forward
                curr = tmp            # Move curr forward
            
            # After reversal:
            # - 'kth' (old last node) is now the new first node of this group
            # - 'groupPrev.next' (old first node) is now the new last node
            
            tmp = groupPrev.next      # Save old first node (now the tail of reversed group)
            groupPrev.next = kth      # Connect previous group to new head (kth)
            groupPrev = tmp           # Move groupPrev to the tail for next iteration
        
        return dummy.next

    def getKth(self, curr, k):
        # Move k steps forward from curr to find the kth node
        # Returns None if fewer than k nodes exist
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
