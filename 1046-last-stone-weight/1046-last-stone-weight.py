import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Goal: Simulate stone smashing until one or zero stones remain
        # Rules: Pick two heaviest stones, smash them together
        #   - If equal weight: both destroyed
        #   - If different: new stone with weight = difference remains
        # Approach: Use max-heap to efficiently get heaviest stones
        # Python only has min-heap, so negate values to simulate max-heap
        
        # Step 1: Convert to max-heap by negating all values
        stones = [-s for s in stones]  # Negate: max becomes min in min-heap
        heapq.heapify(stones)  # Build min-heap in O(n) time
        
        # Step 2: Repeatedly smash two heaviest stones
        while len(stones) > 1:
            # Pop two largest (most negative) stones
            first = heapq.heappop(stones)   # Heaviest stone (most negative)
            second = heapq.heappop(stones)  # Second heaviest (most negative)
            
            # If stones have different weights, create new stone with difference
            if second > first:  # Remember: values are negative, so second > first means |second| < |first|
                heapq.heappush(stones, first - second)  # Difference (still negative)
            # If equal (second == first), both destroyed, nothing added back
        
        # Step 3: Return last stone weight (or 0 if no stones left)
        # Use abs to convert back to positive, handle empty list case
        return abs(stones[0]) if stones else 0  # Fixed: handle empty stones case