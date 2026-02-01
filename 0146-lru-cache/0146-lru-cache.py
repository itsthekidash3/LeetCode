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
        self.cache = {}      # Dictionary to map keys to their corresponding Node

        # Dummy nodes to simplify edge insertions and deletions
        self.prev = Node(0, 0)  # Dummy node representing the LRU end (least recently used)
        self.next = Node(0, 0)  # Dummy node representing the MRU end (most recently used)
        self.prev.next = self.next
        self.next.prev = self.prev
        

    def get(self, key: int) -> int:
        # If key exists in cache, move it to the MRU (most recently used) position
        if key in self.cache:
            self.remove(self.cache[key])   # Remove node from its current position
            self.insert(self.cache[key])   # Re-insert it at the MRU end
            return self.cache[key].val
        # If key not found, return -1
        return -1

    def remove(self, node):
        """
        Removes a node from the doubly linked list.
        This is used when a node is accessed (to update its position)
        or when the LRU node is evicted.
        """
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        """
        Inserts a node at the MRU (most recently used) position, right before the dummy tail (self.next).
        This signifies the node was recently accessed or added.
        """
        prev_node, next_node = self.next.prev, self.next
        prev_node.next = next_node.prev = node  # Link the new node between prev_node and MRU end
        node.next = next_node
        node.prev = prev_node

    def put(self, key: int, value: int) -> None:
        """
        Add a new key-value pair to the cache.
        If key already exists, update the value and move it to MRU position.
        If capacity is exceeded, remove the LRU node.
        """
        if key in self.cache:
            self.remove(self.cache[key])  # Remove old node if key exists
        self.cache[key] = Node(key, value)  # Create new node
        self.insert(self.cache[key])        # Insert it at MRU position

        # If cache exceeds capacity, remove the LRU node (right after dummy head / self.prev)
        if len(self.cache) > self.cap:
            lru = self.prev.next           # Node to remove (LRU)
            self.remove(lru)
            del self.cache[lru.key]       # Remove from dictionary
