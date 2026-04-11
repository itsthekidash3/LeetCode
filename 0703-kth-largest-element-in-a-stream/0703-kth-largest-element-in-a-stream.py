import heapq

class KthLargest:
    # Goal: Maintain kth largest element in a stream of numbers
    # Approach: Min-heap of size k (root is kth largest, all others are larger)
    # Key insight: In a min-heap of k largest elements, the smallest (root) is the kth largest overall
    
    def __init__(self, k: int, nums: List[int]):
        # Initialize with existing numbers
        self.minHeap = nums  # Store all initial numbers
        self.k = k
        
        # Convert list to min-heap in O(n) time
        heapq.heapify(self.minHeap)
        
        # Keep only k largest elements by removing smallest ones
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove smallest element
        
        # Now minHeap contains k largest elements, with kth largest at root

    def add(self, val: int) -> int:
        # Add new value and maintain k largest elements
        heapq.heappush(self.minHeap, val)  # Fixed: should be self.minHeap
        
        # If heap exceeds size k, remove smallest element
        if len(self.minHeap) > self.k:  # Fixed: should be self.minHeap and self.k
            heapq.heappop(self.minHeap)
        
        # Return kth largest (smallest in our k-sized heap)
        return self.minHeap[0]  # Fixed: should be self.minHeap


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Time Complexity:
# - __init__: O(n + (n-k)log(n)) → O(n log n) worst case
#   - heapify: O(n)
#   - pop n-k elements: O((n-k) log n)
# - add: O(log k)
#   - push: O(log k)
#   - pop (if needed): O(log k)

# Space Complexity: O(k)
# - Heap maintains at most k elements after initialization