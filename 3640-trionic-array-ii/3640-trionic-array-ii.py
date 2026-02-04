class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        # suf[i]: maximum sum of a strictly increasing subarray
        # ending exactly at index i
        suf = [nums[0]] * n

        # pre[i]: maximum sum of a strictly decreasing subarray
        # starting exactly at index i
        pre = [nums[-1]] * n

        # Build suf[] from left to right
        for i in range(1, n):
            suf[i] = nums[i]
            # If still increasing, extend the previous increasing subarray
            if nums[i] > nums[i - 1]:
                suf[i] += max(nums[i - 1], suf[i - 1])

        # Build pre[] from right to left
        for i in range(n - 2, -1, -1):
            pre[i] = nums[i]
            # If still decreasing, extend the next decreasing subarray
            if nums[i] < nums[i + 1]:
                pre[i] += max(nums[i + 1], pre[i + 1])

        # arr will store all valid trionic "middle" segments
        # each entry: [peak_index, valley_index, sum_of_middle_decrease]
        i = 1
        arr = []

        while i < n - 1:
            # Identify a peak (end of first increasing part)
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                j = i + 1
                c = 0  # sum of strictly decreasing middle part

                # Traverse the decreasing segment
                while j + 1 < n and nums[j] > nums[j + 1]:
                    c += nums[j]
                    j += 1

                # If we reach the end, cannot form a valid trionic array
                if j == n - 1:
                    break

                # Store peak, valley, and middle sum
                arr.append([i, j, c])

                # Skip processed indices
                i = j
            else:
                i += 1

        # Compute the maximum trionic sum
        res = float("-inf")
        for peak, valley, mid_sum in arr:
            # suf[peak] = left increasing part
            # mid_sum = middle decreasing part
            # pre[valley] = right increasing part
            res = max(res, suf[peak] + pre[valley] + mid_sum)

        return res
