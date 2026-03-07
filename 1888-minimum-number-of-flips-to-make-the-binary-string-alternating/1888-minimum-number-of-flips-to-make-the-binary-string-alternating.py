class Solution:
    def minFlips(self, s: str) -> int:
        # Use sliding window on doubled string (s+s) to check all rotations efficiently
        # Try both alternating patterns (starting with 0 and 1) and track minimum flips needed
        
        n = len(s)
        best = n  # worst case: flip all bits
        S = s + s  # doubled string allows checking all rotations in one pass
        
        # Try both alternating patterns: "010101..." and "101010..."
        for start in [0, 1]:
            count = 0  # number of mismatches in current window
            
            # Sliding window: expand right, shrink from left when size exceeds n
            for right in range(2 * n - 1):
                left = right - n + 1  # left boundary of window (size n)
                
                # Add the right element: check if it mismatches the expected pattern
                if int(S[right]) != (start + right) % 2:
                    count += 1
                
                # Remove the left element: if window exceeds size n, remove leftmost mismatch
                if left >= 1:
                    # Check if the position leaving the window (left-1) was a mismatch
                    if int(S[left - 1]) != (start + left - 1) % 2:
                        count -= 1  # no longer count this mismatch
                
                # Update best: only when we have a valid window (left >= 0 means window started)
                if left >= 0:
                    best = min(best, count)
        
        return best