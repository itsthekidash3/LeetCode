# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Goal: Convert tree to string representation
        # Approach: Preorder DFS traversal (root → left → right)
        # Use "N" to mark null nodes so structure is preserved
        
        res = []  # Store serialized values
        
        def dfs(node):
            # Base case: null node represented as "N"
            if not node:
                res.append("N")
                return
            
            # Preorder: process root, then left, then right
            res.append(str(node.val))  # Add current node value
            dfs(node.left)   # Recursively serialize left subtree
            dfs(node.right)  # Recursively serialize right subtree
        
        dfs(root)
        # Join array into comma-separated string
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Goal: Reconstruct tree from serialized string
        # Approach: Parse values in same preorder sequence used during serialization
        # Use global index to track current position in the value list
        
        vals = data.split(",")  # Split string back into list of values
        self.i = 0  # Global pointer to current position in vals array
        
        def dfs():
            # Base case: "N" means null node
            if vals[self.i] == "N":
                self.i += 1  # Move to next value
                return None
            
            # Create node with current value
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # Move to next value
            
            # Recursively build left and right subtrees (preorder)
            node.left = dfs()   # Next values form left subtree
            node.right = dfs()  # Remaining values form right subtree
            
            return node
        
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))