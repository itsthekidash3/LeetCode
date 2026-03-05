class TimeMap:

    def __init__(self):
        # Initialize a hash map to store key -> list of [value, timestamp] pairs
        # Each key maps to a list that will be naturally sorted by timestamp (since set() is called in order)
        self.store = {}  # key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Store a key-value pair at a specific timestamp
        # Timestamps are guaranteed to be strictly increasing for each key
        
        # Create a new list for this key if it doesn't exist yet
        if key not in self.store:
            self.store[key] = []
        
        # Append the [value, timestamp] pair to the key's list
        # Since timestamps are strictly increasing, the list stays sorted
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # Return the value with the largest timestamp <= given timestamp
        # Use binary search since the timestamp list is sorted
        
        res = ""  # Default return value if no valid timestamp found
        
        # Get the list of [value, timestamp] pairs for this key (empty list if key doesn't exist)
        values = self.store.get(key, [])

        # Binary search to find the largest timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            
            # If this timestamp is valid (not too large), it's a candidate
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # Update result with this value
                l = mid + 1  # Search right half for potentially larger valid timestamp
            else:
                # This timestamp is too large, search left half
                r = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)