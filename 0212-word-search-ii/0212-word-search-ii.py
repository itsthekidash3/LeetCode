class TrieNode:
    def __init__(self):
        self.children = {}  # HashMap of child nodes (key=character, value=TrieNode)
        self.endOfWord = False  # Flag marking if a valid word ends here

    def addWord(self, word):
        # Insert word into trie starting from current node
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create new node if path doesn't exist
            cur = cur.children[c]  # Move to child node
        cur.endOfWord = True  # Mark end of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Goal: Find all words from the list that exist in the board
        # Approach: Build trie from words, then DFS from each cell following trie paths
        # Key insight: Trie allows checking multiple words simultaneously during one DFS
        
        # Step 1: Build trie containing all words to search for
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()  # res = found words (set avoids duplicates)
                                    # visit = cells visited in current path
        
        def dfs(r, c, node, word):
            # r, c: current board position
            # node: current position in trie
            # word: word formed so far along this path
            
            # Base cases: out of bounds, already visited, or character not in trie
            if (r < 0 or c < 0 or 
                r == rows or c == cols or 
                (r, c) in visit or 
                board[r][c] not in node.children):
                return
            
            visit.add((r, c))  # Mark current cell as visited
            
            # Move to trie node corresponding to current board character
            node = node.children[board[r][c]]
            word += board[r][c]  # Append character to current word
            
            # If we've reached end of a valid word in trie, add to results
            if node.endOfWord:
                res.add(word)
            
            # Explore all 4 directions (up, down, left, right)
            dfs(r - 1, c, node, word)  # Up
            dfs(r + 1, c, node, word)  # Down
            dfs(r, c - 1, node, word)  # Left
            dfs(r, c + 1, node, word)  # Right
            
            visit.remove((r, c))  # Backtrack: unmark cell for other paths
        
        # Step 2: Try starting DFS from every position on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")  # Start with empty word at trie root
        
        return list(res)  # Convert set to list for return