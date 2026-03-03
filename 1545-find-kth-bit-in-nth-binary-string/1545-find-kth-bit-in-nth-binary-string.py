class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Convert k to 0-indexed for easier math
        k -= 1

        def f(N, K):
            # Base case: S1 = "0", only one character
            if N == 1:
                return 0

            left_len = pow(2, N-1) - 1   # length of each half (excluding middle)
            mid_idx  = left_len           # 0-indexed position of the middle '1'

            # Case 1: K falls in the LEFT half → same as asking S(N-1) at position K
            if K < mid_idx:
                return f(N-1, K)

            # Case 2: K is exactly the MIDDLE element, which is always '1'
            if K == mid_idx:
                return 1

            # Case 3: K falls in the RIGHT half
            # The right half is reverse(invert(S(N-1))), so:
            #   - Find the offset from the start of the right half
            #   - Mirror it to the corresponding index in the left half
            #   - Flip the bit (1 - ...)
            right_offset = K - mid_idx - 1              # offset within the right half
            mirrored_idx = left_len - 1 - right_offset  # corresponding index in left half
            return 1 - f(N-1, mirrored_idx)

        return str(f(n, k))