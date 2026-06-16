# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead =   ListNode(-1, head)

        fast = newHead
        slow = newHead
        prev = 0

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = prev.next.next
        return newHead.next    