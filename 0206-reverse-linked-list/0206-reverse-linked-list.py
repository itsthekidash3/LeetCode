# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # prev pointer is set to null
        curr = head # initalize current to the first node to set it a the last
        while curr:
            # at the curr node
            nxt = curr.next # temp variable
            curr.next = prev # pointing to prev
            # need to shift the node after iteration
            prev = curr # shift it to current 
            # curr = curr.next
            # need a temp variable to store the next , coz we are breaking the pointer
            curr = nxt # shift it to the next
        
        return prev

        