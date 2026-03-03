class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Array is sorted but rotated.
        # One half is always sorted.
        # We use binary search to find the pivot (minimum).

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:

            # If current window is already sorted,
            # the leftmost element is the minimum.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            # If middle is in left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Middle is in right sorted portion
                r = m - 1

        return res