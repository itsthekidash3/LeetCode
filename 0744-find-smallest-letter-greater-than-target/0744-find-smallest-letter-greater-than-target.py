class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # We want the FIRST letter that is strictly greater than target.
        # This is a binary search on a sorted array (bisect_right behavior).

        l, r = 0, len(letters)
        # Invariant: the answer is always in the range [l, r)

        while l < r:
            # Pick the middle index of the current search range
            mid = l + (r - l) // 2

            if letters[mid] > target:
                # mid could be the answer, so keep it in the search space
                r = mid
            else:
                # letters[mid] <= target
                # mid cannot be the answer, so discard it and everything before it
                l = mid + 1

        # If l runs past the end, wrap around (problem requirement)
        if l == len(letters):
            return letters[0]

        # Otherwise, l points to the first letter > target
        return letters[l]
