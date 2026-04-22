# borrowed code from vkram

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # Goal: Find queries that are within 2 character differences from any dictionary word
        # Approach 1: Brute force - compare each query with each dictionary word
        # Time: O(Q × D × L) where Q=queries, D=dictionary, L=word length
        
        ans = []
        
        # For each query word
        for q in queries:
            # Check against each dictionary word
            for d in dictionary:
                diff = 0  # Count character differences
                
                # Compare character by character
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1
                    
                    # Early termination: more than 2 differences
                    if diff > 2:
                        break
                
                # If within 2 edits, add query and move to next query
                if diff <= 2:
                    ans.append(q)
                    break  # Found match, no need to check other dictionary words
        
        return ans


# ========== OPTIMAL SOLUTION: TRIE WITH DFS ==========
# class Solution:
#     class Trie:
#         def __init__(self):
#             # Each node has 26 children (one for each letter a-z)
#             self.child = [None] * 26
#             self.end = False  # Marks end of a dictionary word
#     
#     def __init__(self):
#         self.root = self.Trie()  # Initialize empty trie
#     
#     def insert(self, s):
#         # Insert dictionary word into trie
#         node = self.root
#         for c in s:
#             i = ord(c) - ord('a')  # Convert char to index 0-25
#             if not node.child[i]:
#                 node.child[i] = self.Trie()  # Create new node if doesn't exist
#             node = node.child[i]  # Move to child node
#         node.end = True  # Mark end of word
#     
#     def dfs(self, s, idx, node, edits):
#         # DFS search through trie allowing up to 2 mismatches
#         # s: query word
#         # idx: current position in query word
#         # node: current position in trie
#         # edits: number of edits used so far
#         
#         # Pruning: More than 2 edits used
#         if edits > 2:
#             return False
#         
#         # Base case: Reached end of query word
#         if idx == len(s):
#             return node.end  # True if this is end of a dictionary word
#         
#         # Try all 26 possible characters at this position in trie
#         for i in range(26):
#             if node.child[i]:  # If this child exists in trie
#                 # Calculate if this character matches query character
#                 # If mismatch, increment edits
#                 newEdit = edits + (i != (ord(s[idx]) - ord('a')))
#                 
#                 # Recursively search next position
#                 if self.dfs(s, idx + 1, node.child[i], newEdit):
#                     return True  # Found match within 2 edits
#         
#         return False  # No match found
#     
#     def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
#         # Build trie from dictionary words
#         for w in dictionary:
#             self.insert(w)
#         
#         ans = []
#         
#         # For each query, search trie with up to 2 edits allowed
#         for q in queries:
#             if self.dfs(q, 0, self.root, 0):  # Start DFS from root with 0 edits
#                 ans.append(q)
#         
#         return ans