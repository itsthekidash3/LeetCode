# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next is None:
            return head.val + head.next.val

        result = [0]
        q = [None]

        self.traverse(head, head, result, q)
        return result[0]

    def traverse(self, head, p, result, q):

        if p is not None:
            q[0] = head.next

            self.traverse(head.next,p.next.next,result,q)

            result[0] = max(result[0],head.val + q[0].val)
            q[0] = q[0].next