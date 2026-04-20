class Solution:
    def maxDistance(self, A: List[int]) -> int:
        # Goal: Find maximum distance between different values in binary array
        # Approach: Find furthest position from start that differs from A[0]
        #           AND furthest position from end that differs from A[-1]
        # Key insight: In binary array, max distance is either:
        #   - From leftmost position where value != A[-1] to end
        #   - From start to rightmost position where value != A[0]
        
        n = len(A)
        left, right = 0, n - 1  # Initialize to array boundaries
        
        # Find leftmost index where value differs from last element
        # This gives us the starting point for maximum distance to end
        for i in range(n):
            if A[i] ^ A[-1]:  # XOR: True if different, False if same
                left = i
                break
        
        # Find rightmost index where value differs from first element
        # This gives us the ending point for maximum distance from start
        for i in range(n - 1, -1, -1):  # Traverse backwards
            if A[i] ^ A[0]:  # XOR: True if different, False if same
                right = i
                break
        
        # Return maximum of two possible distances:
        # 1. Distance from leftmost different-from-last to end: (n-1) - left
        # 2. Distance from start to rightmost different-from-first: right - 0
        return max(n - 1 - left, right)