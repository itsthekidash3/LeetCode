class Solution:
    def smallestBalancedIndex(self, nums):
        n = len(nums)
        LIMIT = 100000000000000  # 1e14

        suffix = [1] * n
        prod = 1

        for i in range(n - 2, -1, -1):
            if prod > LIMIT // nums[i + 1]:
                prod = LIMIT + 1
            else:
                prod *= nums[i + 1]
            suffix[i] = prod

        total_sum = 0
        for i in range(n):
            if total_sum == suffix[i]:
                return i
            total_sum += nums[i]

        return -1