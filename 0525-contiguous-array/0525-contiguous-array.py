class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # hmap maps a prefix sum value -> the FIRST index where it appeared
        # prefix sum = (# of 1s) - (# of 0s) up to current index
        hmap = {}

        # sumMax keeps the running prefix sum
        sumMax = 0

        # maxLength stores the longest subarray found so far
        maxLength = 0

        for i, n in enumerate(nums):
            # Treat 1 as +1 and 0 as -1
            # This allows equal 0s and 1s to sum to 0
            sumMax += 1 if n == 1 else -1

            # If prefix sum is 0, subarray from index 0 to i
            # has equal number of 0s and 1s
            if sumMax == 0:
                maxLength = i + 1

            # If we've seen this prefix sum before,
            # the subarray between the previous index and current index
            # has net sum 0 → equal 0s and 1s
            if sumMax in hmap:
                maxLength = max(maxLength, i - hmap[sumMax])
            else:
                # Store the FIRST occurrence of this prefix sum
                # (earliest index gives the longest possible subarray)
                hmap[sumMax] = i

        return maxLength
