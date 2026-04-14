class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Goal: Find kth largest element in unsorted array
        # Approaches:
        #   1. Sort and index: O(n log n) time, O(1) or O(n) space
        #   2. Min heap: O(n log k) time, O(k) space
        #   3. Quick Select: O(n) average time, O(1) space


    # ========== APPROACH 1: SORT AND INDEX ==========
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # Goal: Sort array and return kth largest element
    #     # Time: O(n log n) - dominated by sorting
    #     # Space: O(1) if in-place sort, O(n) if using Timsort (Python's default)
    #     
         nums.sort()  # Sort in ascending order
    #     # kth largest is at index (n-k) in sorted array
         return nums[len(nums) - k]


    # ========== APPROACH 2: MIN HEAP OF SIZE K ==========
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # Goal: Maintain heap of k largest elements, root is kth largest
    #     # Time: O(n log k) - n insertions/pops, each O(log k)
    #     # Space: O(k) - heap size limited to k elements
    #     
    #     import heapq
    #     
    #     # Build min-heap with first k elements
    #     minHeap = nums[:k]
    #     heapq.heapify(minHeap)  # O(k) time
    #     
    #     # Process remaining elements
    #     for i in range(k, len(nums)):
    #         # If current element is larger than smallest in heap (root)
    #         if nums[i] > minHeap[0]:
    #             heapq.heappop(minHeap)      # Remove smallest
    #             heapq.heappush(minHeap, nums[i])  # Add current element
    #     
    #     # Root of min-heap is kth largest element
    #     return minHeap[0]


    # ========== APPROACH 2 ALTERNATIVE: MAX HEAP ==========
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # Goal: Use max-heap to extract k largest elements
    #     # Time: O(n + k log n) - heapify O(n), k pops O(k log n)
    #     # Space: O(n) - full heap
    #     
    #     import heapq
    #     
    #     # Python only has min-heap, negate values for max-heap behavior
    #     maxHeap = [-num for num in nums]
    #     heapq.heapify(maxHeap)  # O(n) time
    #     
    #     # Pop k-1 largest elements
    #     for _ in range(k - 1):
    #         heapq.heappop(maxHeap)
    #     
    #     # kth largest is now at root
    #     return -heapq.heappop(maxHeap)  # Negate back to positive

            
    # ========== APPROACH 3: QUICK SELECT (MAIN SOLUTION) ==========
    # Convert "kth largest" to "index in sorted array"
    # kth largest = (n-k)th smallest in 0-indexed sorted array
    
    
    
    #   k_index = len(nums) - k
        
    #    def quickSelect(l, r):
            # Partition array around pivot, return kth smallest element
            # Uses Lomuto partition scheme
            
    #        pivot = nums[r]  # Choose rightmost element as pivot
    #        p = l  # Partition index: elements before p are ≤ pivot
            
    #        # Partition: move elements ≤ pivot to left side
    #        for i in range(l, r):
    #            if nums[i] <= pivot:
    #                nums[p], nums[i] = nums[i], nums[p]  # Swap to left partition
    #                p += 1
            
            # Place pivot in its final sorted position
    #        nums[p], nums[r] = nums[r], nums[p]
            
            # p is now the index where pivot belongs in sorted array
            # Recursively search the partition containing kth element
    #        if p > k_index:
    #            return quickSelect(l, p - 1)
    #        elif p < k_index:
    #            return quickSelect(p + 1, r)
    #        else:
    #            return nums[p]  # Found kth element
        
    #    return quickSelect(0, len(nums) - 1)
