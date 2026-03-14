class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        # Thought process:
        # - Need to find even numbers that appear exactly once
        # - Need the FIRST one (earliest by index)
        # - Must check entire array to count frequencies
        # - Hash map is perfect: O(1) lookups, stores counts
        
        # Step 1: Build frequency map
        # Time: O(n), Space: O(n) where n is array length
        hMap = {}
        for num in nums:
            hMap[num] = hMap.get(num, 0) + 1  # Count occurrences
        
        # Step 2: Find first even number with count == 1
        # Iterate through original array to preserve order
        for num in nums:
            if num % 2 == 0 and hMap[num] == 1:  # Check: even AND unique
                return num  # Return immediately (first occurrence)
        
        # Step 3: No valid number found
        return -1

        