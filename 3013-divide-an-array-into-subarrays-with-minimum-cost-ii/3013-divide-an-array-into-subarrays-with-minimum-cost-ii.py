class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # We always take nums[0] as the cost of the first subarray
        # That subarray is fixed, so subtract 2:
        #  - one for nums[0]
        #  - one because we only care about choosing k-1 other starts,
        #    and the window logic handles k-1 as (k-2 additional picks)
        k -= 2

        # Remove nums[0] and lock it into the total cost
        cost = nums.pop(0)

        # Answer we want to minimize
        res = float('inf')

        # Maintain a sliding window of size `dist`
        # This window represents valid positions where subarrays can start
        # SortedList lets us quickly get the smallest elements
        window = SortedList(nums[:dist])

        # Initially, take the smallest `k` elements from the window
        # These represent the cheapest possible starts for subarrays
        cost += sum(window[:k])

        # Slide the window across nums
        # left  -> element leaving the window
        # right -> element entering the window
        for left, right in zip(nums, nums[dist:]):

            # Add the new element to the sorted window
            window.add(right)

            # If `right` is among the smallest k elements,
            # it may replace the k-th smallest value
            # window[k] is the (k+1)-th smallest element
            cost += min(window[k], right)

            # Update the minimum result
            res = min(res, cost)

            # Remove the contribution of the outgoing element (`left`)
            # If `left` was part of the k smallest, it affected cost
            cost -= min(window[k], left)

            # Remove `left` from the window
            window.remove(left)

        return res
