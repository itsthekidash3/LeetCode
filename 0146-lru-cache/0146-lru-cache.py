# LRU Cache: Combine HashMap + Doubly Linked List
# HashMap: O(1) lookup by key
# Doubly Linked List: O(1) removal and insertion to track recency order
# Left (LRU end) ← ... ← Right (MRU end)
# Most recently used items are near right, least recently used near left

# Node class for doubly linked list
# Each node stores a key-value pair and pointers to previous and next nodes
class Node:
    def __init__(self, key, val):
        self.key = key       # The key of the cache entry
        self.val = val       # The value of the cache entry
        self.prev = None     # Pointer to the previous node in the linked list
        self.next = None     # Pointer to the next node in the linked list

# LRUCache class implementing Least Recently Used cache
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # Maximum capacity of the cache
        self.cache = {}      # HashMap: maps keys to their corresponding Node for O(1) lookup

        # Dummy nodes to simplify edge case handling (no null checks needed)
        self.left = Node(0, 0)   # Dummy head - LRU end (least recently used)
        self.right = Node(0, 0)  # Dummy tail - MRU end (most recently used)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        """
        Helper: Remove a node from the doubly linked list (O(1))
        Used when accessing a node (to reposition) or evicting LRU node
        """
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        """
        Helper: Insert node at MRU position (right before dummy tail) (O(1))
        Signifies the node was just accessed or added - mark as most recently used
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node  # Link the new node between prev and right
        node.next = nxt
        node.prev = prev
        
    def get(self, key: int) -> int:
        """
        Get value by key. If exists, move to MRU position (was just accessed)
        Return -1 if key not found
        """
        if key in self.cache:
            self.remove(self.cache[key])   # Remove from current position
            self.insert(self.cache[key])   # Re-insert at MRU end (mark as recently used)
            return self.cache[key].val
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        """
        Add/update key-value pair. Always move to MRU position
        If capacity exceeded, evict LRU node (left.next)
        """
        if key in self.cache:
            self.remove(self.cache[key])  # Remove old node if updating
        
        self.cache[key] = Node(key, value)  # Create new node in HashMap
        self.insert(self.cache[key])        # Insert at MRU end

        # If over capacity, remove LRU node (right after dummy head)
        if len(self.cache) > self.cap:
            lru = self.left.next           # LRU node is right after left dummy
            self.remove(lru)               # Remove from linked list
            del self.cache[lru.key]        # Remove from HashMap