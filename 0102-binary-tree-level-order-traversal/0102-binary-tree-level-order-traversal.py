# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # go level wise
        # BFS algo
        # use queue
        # fifo

        res = []
        q = collections.deque()
        q.append(root)

        # run BFS , while queue is non empty

        while q:
            qLen = len(q) # no of values in the queue currently
            # going through one level at a time
            level=[]
            # loop through every value in the list
            for i in range(qLen):
                node = q.popleft()
                if node: #checking if node is null Edge case
                    level.append(node.val) # from node
                    q.append(node.left) # append nodes left
                    q.append(node.right) # append nodes right
            
            if level:
                res.append(level)
        
        return res


         
        