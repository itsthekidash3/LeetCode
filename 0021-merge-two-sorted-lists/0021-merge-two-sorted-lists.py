# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (no need to check if head is None)
        # This acts as a placeholder; the actual merged list starts at dummy.next
        dummy = ListNode()
        tail = dummy  # tail pointer tracks the end of our merged list
        
        
        while list1 and list2:  # Continue while both lists have nodes
            # Compare values and attach the smaller node to our merged list
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2
                list2 = list2.next  # Move list2 pointer forward
            
            tail = tail.next  # Move tail pointer to the newly added node
        
        # After the loop, at most one list has remaining nodes
        # Attach whichever list still has nodes (or None if both are empty)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Return dummy.next because dummy itself is just a placeholder
        return dummy.next