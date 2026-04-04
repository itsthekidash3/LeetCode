class TrieNode():
    def __init__(self):  # Fixed: was _init_ (missing underscores)
        self.children = {}  # HashMap to store child nodes (key=character, value=TrieNode)
        self.endOfWord = False  # Flag marking if a word ends at this node
        # Character not stored in node - it's implicit from parent's children map key

class Trie:

    def __init__(self):
        # Initialize root as empty TrieNode (represents start of all words)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Goal: Add word to trie, creating nodes for each character in path
        # Mark final node as end of word
        
        cur = self.root  # Start at root
        
        # Traverse/create path for each character
        for c in word:
            # If character path doesn't exist, create new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to child node for this character
            cur = cur.children[c]
        
        # After processing all characters, mark end of word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Goal: Check if exact word exists in trie
        # Must reach end AND endOfWord flag must be True
        
        cur = self.root  # Start at root
        
        # Follow path for each character
        for c in word:
            # If character path doesn't exist, word not in trie
            if c not in cur.children:
                return False
            # Move to child node for this character
            cur = cur.children[c]
        
        # Word exists only if we're at a node marked as end of word
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Goal: Check if any word in trie starts with prefix
        # Just need to follow path - don't check endOfWord flag
        
        cur = self.root  # Start at root
        
        # Follow path for each character in prefix
        for c in prefix:
            # If character path doesn't exist, no words with this prefix
            if c not in cur.children:
                return False
            # Move to child node for this character
            cur = cur.children[c]
        
        # Prefix exists if we successfully followed entire path
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)