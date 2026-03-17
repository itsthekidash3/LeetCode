# went through larrys solution to solve the problem
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # THOUGHT PROCESS:
        # - Can rearrange columns in any order (key insight!)
        # - Need to find max area where every element is 1
        # - For each cell, track "how many consecutive 1s vertically ending here?"
        #   This gives us the HEIGHT of potential rectangles
        # - After sorting these heights per row, we can try different WIDTHS
        # - Not a DP problem - just preprocessing + greedy sorting!
        
        # APPROACH:
        # 1. Build a "streak" array tracking consecutive 1s in each column
        # 2. For each row, sort the streaks (simulates optimal column rearrangement)
        # 3. Try all possible widths: width × height[width-1]
        
        R = len(matrix)
        C = len(matrix[0])
        
        best = 0
        streak = [0] * C  # Tracks consecutive 1s ending at current row for each column
        
        for i in range(R):
            # Step 1: Update streaks for current row
            for j in range(C):
                if matrix[i][j] == 1:
                    streak[j] += 1  # Extend the streak
                else:
                    streak[j] = 0   # BUG FIX: should be = not ==
            
            # Step 2: Sort streaks to simulate optimal column arrangement
            cells = sorted(streak, reverse=True)  # BUG FIX: 'streak' not 'streal'
            
            # Step 3: Try all possible widths for this row
            for index, value in enumerate(cells, start=1):
                # index = width (how many columns we're using)
                # value = height (tallest rectangle these columns can form)
                best = max(best, index * value)  # BUG FIX: 'value' not 'v'
        
        return best