class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Find median of two sorted arrays in O(log(min(m,n))) time
        # Key insight: Use binary search to partition arrays so left half has (roughly) same elements as right half
        # We want: all elements in left partition <= all elements in right partition
        
        # Strategy:
        # 1. Partition nums1 at index i, partition nums2 at index j
        # 2. Left partition = nums1[0:i+1] + nums2[0:j+1], should have ~half total elements
        # 3. Check if max(left partition) <= min(right partition) for valid partition
        # 4. Adjust binary search pointers until we find the correct partition
        # 5. Median = middle element(s) at the partition boundary
        
        def sol(num1, num2):
            total = len(num1) + len(num2)
            half = total // 2  # Target size of left partition
            
            # Binary search on num1 to find correct partition point
            l, r = 0, len(num1) - 1
            while True:
                # i = partition index in num1 (num1[0] to num1[i] goes to left partition)
                i = (l + r) // 2
                
                # j = partition index in num2 (calculated so left partition has 'half' elements total)
                # half = (i+1) + (j+1), so j = half - i - 2
                j = half - i - 2
                
                # Get boundary values (use -inf/inf for out of bounds)
                # num1left = rightmost element of num1's left partition
                num1left = num1[i] if i >= 0 else float("-inf")
                # num1right = leftmost element of num1's right partition
                num1right = num1[i + 1] if (i + 1) < len(num1) else float("inf")
                # num2left = rightmost element of num2's left partition
                num2left = num2[j] if j >= 0 else float("-inf")
                # num2right = leftmost element of num2's right partition
                num2right = num2[j + 1] if (j + 1) < len(num2) else float("inf")
                
                # Check if partition is correct:
                # All elements in left partition should be <= all elements in right partition
                if num1left <= num2right and num2left <= num1right:
                    # Correct partition found!
                    
                    # Odd total elements: median is the smallest element in right partition
                    if total % 2:
                        return min(num1right, num2right)
                    
                    # Even total elements: median is average of largest left and smallest right
                    return (max(num1left, num2left) + min(num1right, num2right)) / 2
                
                # Partition incorrect: adjust binary search pointers
                elif num1left > num2right:
                    # num1's left partition has elements too large
                    # Move partition point left in num1 (take fewer elements from num1)
                    r = i - 1
                else:
                    # num2's left partition has elements too large (num2left > num1right)
                    # Move partition point right in num1 (take more elements from num1)
                    l = i + 1
        
        # Always binary search on the smaller array for efficiency
        if len(nums1) <= len(nums2):
            return sol(nums1, nums2)
        else:
            return sol(nums2, nums1)