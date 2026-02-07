class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Initial thought process:
        # ------------------------
        # We want to remove the minimum number of characters so that
        # the string has NO pattern of "ba"
        # i.e. no pair (i, j) such that i < j, s[i] = 'b', s[j] = 'a'
        #
        # First ideas considered:
        # - brute force pairs → O(n^2) (too slow)
        # - pointers / sliding window? hard to maintain correctness
        # - DP? maybe, but feels overkill
        # - stack? hashmap? unnecessary
        #
        # Observation:
        # Valid final string must look like:
        #   aaaa...bbbb
        #
        # So every time we see an 'a' AFTER a 'b', something must be deleted.

        count = 0   # number of 'b's seen so far (potential violations)
        res = 0     # total deletions needed

        for ch in s:
            if ch == 'b':
                # Track how many 'b's we have before the current index.
                # These 'b's are fine for now, but could cause issues
                # if an 'a' appears later.
                count += 1

            elif count:
                # We found an 'a' AFTER at least one 'b' → "ba" violation
                #
                # Two choices:
                # 1. Delete this 'a' (cost = 1)
                # 2. Delete all previous 'b's (cost = count)
                #
                # Greedy insight:
                # Deleting ONE 'a' is always cheaper than deleting
                # multiple 'b's, so we delete this 'a'.
                res += 1

                # Conceptually, this deletion "handles" one bad 'b'
                # because we chose to keep the rest of the order intact
                count -= 1

        # res now contains the minimum deletions required
        return res
