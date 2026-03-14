# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # APPROACH 1: Hash Set - Store visited nodes, check if we see one twice
        # Time: O(n), Space: O(n) - simple but uses extra memory
        
        # APPROACH 2: Floyd's Tortoise and Hare (implemented below)
        # Use two pointers: slow moves 1 step, fast moves 2 steps
        # If there's a cycle, fast will eventually "lap" slow and they'll meet
        # If there's no cycle, fast will reach the end (None)
        # Time: O(n), Space: O(1) - optimal!
        
        slow, fast = head, head
        
        # Key: Check "fast and fast.next" to avoid NoneType errors
        # We need fast.next to exist because we do fast.next.next
        while fast and fast.next:
            slow = slow.next          # Move slow by 1
            fast = fast.next.next     # Move fast by 2
            
            if fast == slow:          # Pointers met - cycle detected!
                return True
        
        # Fast reached the end - no cycle exists
        return False