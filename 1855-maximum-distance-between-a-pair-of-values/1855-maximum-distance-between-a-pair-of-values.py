class Solution:
    def maxDistance(self, A: List[int], B: List[int]) -> int:
        # Goal: Find maximum distance j - i where A[i] <= B[j]
        # Approach: Two pointers - increment i only when A[i] > B[j]
        # Key insight: Both arrays are sorted, so we can greedily expand distance
        
        i, j = 0, 0  
        
        # Traverse B with pointer j, move i only when constraint violated
        while i < len(A) and j < len(B):
            # If A[i] > B[j], constraint violated - must move i forward
            # Otherwise A[i] <= B[j], valid pair - keep i, expand j
            i += A[i] > B[j]  # Increment i by 1 if True (1), 0 if False (0)
            j += 1  # Always move j forward to maximize distance
        
        # Maximum distance found
        # j-1 because j incremented one extra time after last valid pair
        # Subtract i to get distance
        return j - i - 1


# ========== ALTERNATIVE: MORE READABLE VERSION ==========
# class Solution:
#     def maxDistance(self, A: List[int], B: List[int]) -> int:
#         # Goal: Find max(j - i) where i <= j and A[i] <= B[j]
#         # Both arrays are sorted in non-decreasing order
#         
#         i = 0  # Pointer for array A
#         max_dist = 0
#         
#         # Try each position in B
#         for j in range(len(B)):
#             # If current A[i] > B[j], move i forward
#             # We need A[i] <= B[j] for valid pair
#             while i < len(A) and A[i] > B[j]:
#                 i += 1
#             
#             # If we found valid i (A[i] <= B[j]), calculate distance
#             if i < len(A):
#                 max_dist = max(max_dist, j - i)
#         
#         return max_dist