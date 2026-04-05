# Initialize a trie node

class TrieNode:
    def __init__(self):
        self.children = {}  # Fixed typo: was 'childresn'
        self.endOfWord = False  # Flag marking end of a valid word

class WordDictionary: 
    # Goal: Implement word dictionary with wildcard search support
    # Approach: Trie for storage, DFS with backtracking for wildcard '.' search

    def __init__(self):
        self.root = TrieNode()  # Initialize empty trie
        

    def addWord(self, word: str) -> None:
        # Goal: Insert word into trie (same as standard trie insert)
        
        cur = self.root
        
        # Traverse/create path for each character
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create new node if path doesn't exist
            cur = cur.children[c]  # Move to child node
        
        # Mark end of word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Goal: Search for word with wildcard support ('.' matches any character)
        # Approach: DFS to explore all possible paths when '.' is encountered
        
        def dfs(j, root):
            # j: current position in word
            # root: current trie node we're at
            
            cur = root
            
            # Process remaining characters from position j
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':  # Wildcard: must try all possible children
                    # Explore each child node (any character could match)
                    for child in cur.children.values():  # .values() gives TrieNode objects
                        # Recursively search from next position with this child
                        if dfs(i + 1, child):  # Skip wildcard, continue from i+1
                            return True  # Found match in one of the paths
                    
                    return False  # No path matched the remaining pattern
                
                else:  # Regular character: standard trie search
                    if c not in cur.children:  # Character path doesn't exist
                        return False
                    cur = cur.children[c]  # Move to child node for this character
            
            # Processed all characters - check if we're at end of a valid word
            return cur.endOfWord  # Fixed: was cur.word, should be cur.endOfWord
        
        # Start DFS from position 0 at root
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)