# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal or pre order traversal?
        # DFS
        # check boundary
        

        def isValid(node, leftB, rightB):
            if not node:
                return True
            if not (node.val < rightB and node.val > leftB):
                return False
            return (isValid(node.left,leftB,node.val) and
            isValid(node.right,node.val, rightB))
        
        return isValid(root, float("-inf"),float("inf"))

