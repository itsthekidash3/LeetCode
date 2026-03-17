# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as reversed linked lists.
        Example: 342 + 465 = 807 → [2,4,3] + [5,6,4] = [7,0,8]
        
        Strategy: Digit-by-digit addition with carry
        - Process both lists simultaneously (like grade-school addition)
        - Handle different lengths by treating missing digits as 0
        - Track carry and continue until both lists AND carry are done
        """
        
        dummy = ListNode()  # Placeholder to simplify result list building
        curr = dummy        # Pointer to build the result list
        carry = 0           # Tracks carry-over from previous digit addition
        
        # Continue while there are digits in either list OR carry remains
        # Example: [9,9] + [1] needs 3 iterations (9+1=10, 9+0=9, carry=1)
        while l1 or l2 or carry:
            # Extract current digit values (0 if list exhausted)
            v1 = l1.val if l1 else 0  # Handles diff lengths: missing = 0
            v2 = l2.val if l2 else 0
            
            # Add current digits + carry from previous step
            val = v1 + v2 + carry
            carry = val // 10  # Extract tens place (0 or 1)
            val = val % 10     # Extract ones place (the digit we store)
            
            # Example: 8 + 7 + 0 = 15 → carry=1, val=5
            
            # Create new node with the ones digit
            curr.next = ListNode(val)
            
            # Advance all pointers
            curr = curr.next
            l1 = l1.next if l1 else None  # Advance or stay None if exhausted
            l2 = l2.next if l2 else None
        
        # dummy.next is the actual head of result list
        return dummy.next