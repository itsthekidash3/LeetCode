class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Goal: Make all elements equal by adding/subtracting x, minimize operations
        # Approach: Flatten grid, check if possible, find median, calculate operations
        # Key insight: Median minimizes sum of absolute differences
        
        arr = []
        
        # Step 1: Flatten 2D grid into 1D array
        for row in grid:
            for v in row:
                arr.append(v)
        
        # Step 2: Check if all elements can be made equal
        # For elements to reach same value with steps of x:
        # All differences must be divisible by x
        # Equivalently: all elements must have same remainder when divided by x
        base = arr[0]
        for v in arr:
            if abs(v - base) % x != 0:
                return -1  # Impossible to make all equal
        
        # Step 3: Sort array to find median
        arr.sort()
        
        # Step 4: Find median (optimal target value)
        # Median minimizes sum of absolute deviations
        median = arr[len(arr) // 2]
        
        # Step 5: Count total operations needed
        # Each element needs |element - median| / x operations
        ops = 0
        for v in arr:
            ops += abs(v - median) // x
        
        return ops