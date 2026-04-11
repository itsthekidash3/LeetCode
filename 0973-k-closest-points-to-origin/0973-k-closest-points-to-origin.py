import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Goal: Find k closest points to origin (0, 0)
        # Distance formula: sqrt(x^2 + y^2), but we can skip sqrt for comparison
        # Approach: Use min-heap to get k smallest distances efficiently
        
        # Step 1: Build heap with distances and points
        minHeap = []
        for x, y in points:
            # Calculate Euclidean distance squared (skip sqrt since order is preserved)
            dist = (x ** 2) + (y ** 2)
            # Store [distance, x, y] - heap sorts by first element (distance)
            minHeap.append([dist, x, y])
        
        # Step 2: Convert list to min-heap in O(n) time
        heapq.heapify(minHeap)
        
        res = []  # Store k closest points
        
        # Step 3: Extract k smallest distances from heap
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Pop point with smallest distance
            res.append([x, y])  # Add point coordinates (not distance) to result
            k -= 1
        
        return res