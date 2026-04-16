import heapq

class MedianFinder:
    # Goal: Maintain running median of a stream of numbers
    # Approach: Two heaps - max heap for smaller half, min heap for larger half
    # Key insight: Median is at the "middle" - either top of one heap or average of both tops
    
    def __init__(self):
        # small: max heap (stores smaller half of numbers)
        # - Python only has min heap, so negate values to simulate max heap
        # - Top element (self.small[0]) is the largest of the smaller half
        self.small = []  # Max heap: negated values
        
        # large: min heap (stores larger half of numbers)
        # - Top element (self.large[0]) is the smallest of the larger half
        self.large = []  # Min heap: regular values
        
        # Invariants to maintain:
        # 1. Every number in small <= every number in large
        # 2. Size difference between heaps is at most 1

    def addNum(self, num: int) -> None:
        # Goal: Add number and maintain median efficiently
        
        # Step 1: Always add to small heap first (max heap, so negate)
        heapq.heappush(self.small, -1 * num)
        
        # Step 2: Ensure every number in small <= every number in large
        # Check: largest in small (self.small[0] negated) vs smallest in large (self.large[0])
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            # Violation: largest in small is bigger than smallest in large
            # Move the max from small to large
            val = -1 * heapq.heappop(self.small)  # Fixed: heappop doesn't take index
            heapq.heappush(self.large, val)
        
        # Step 3: Balance heap sizes (difference should be at most 1)
        
        # If small heap is too large, move its max to large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)  # Fixed: heappop doesn't take index
            heapq.heappush(self.large, val)
        
        # If large heap is too large, move its min to small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Goal: Return median based on current heap sizes
        
        # Case 1: Odd total count - small heap has one extra element
        if len(self.small) > len(self.large):
            return -1 * self.small[0]  # Negate to get actual max value
        
        # Case 2: Odd total count - large heap has one extra element
        if len(self.large) > len(self.small):
            return self.large[0]  # Min heap top is already positive
        
        # Case 3: Even total count - median is average of both tops
        return ((-1 * self.small[0]) + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()