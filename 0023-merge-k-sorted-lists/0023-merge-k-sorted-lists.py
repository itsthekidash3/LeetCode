# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: empty input
        if not lists or len(lists) == 0:
            return None  # Fixed: should return None, not 0
    
        # Divide-and-conquer: repeatedly merge pairs until one list remains
        while len(lists) > 1:
            mergedLists = []

            # Process lists in pairs (0-1, 2-3, 4-5, etc.)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Handle odd number of lists - last one pairs with None
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            
            # Replace original lists with merged pairs (halves the count each round)
            lists = mergedLists
        
        return lists[0]
    
    
    def mergeList(self, l1, l2):
        # Helper: merge two sorted linked lists
        dummy = ListNode()  # Sentinel node to simplify edge cases
        tail = dummy  # Pointer to build the merged list

        while l1 and l2:
            # Compare heads and attach the smaller one
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:  # Fixed: should be 'else', not 'if l2.val < l1.val'
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # Move tail forward
        
        # Attach remaining nodes (at most one list is non-empty)
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next  # Skip dummy node