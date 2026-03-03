from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko’s speed k must be between 1 and max(piles)
        l, r = 1, max(piles)
        res = r  # store minimum valid speed

        while l <= r:
            k = (l + r) // 2  # candidate eating speed
            hours = 0

            # Calculate total hours needed at speed k
            for p in piles:
                hours += ceil(p / k)

            if hours <= h:
                # k works → try smaller speed
                res = k
                r = k - 1
            else:
                # k too slow → increase speed
                l = k + 1

        return res