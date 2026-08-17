class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + stoneValue[i - 1]

        def search(left_bound: int, right_bound: int) -> int:
            total = prefix[right_bound + 1] - prefix[left_bound]
            start = left_bound

            left = left_bound
            right = right_bound

            while left < right:
                mid = left + (right - left) // 2
                left_sum = prefix[mid + 1] - prefix[start]

                if left_sum * 2 >= total:
                    right = mid
                else:
                    left = mid + 1

            return left

        dp = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]

        for i in range(n):
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]

        for length in range(1, n):
            for i in range(n - length):
                j = i + length

                k = search(i, j)

                total = prefix[j + 1] - prefix[i]
                left_half = prefix[k + 1] - prefix[i]

                if left_half * 2 == total:
                    dp[i][j] = max(
                        left[i][k],
                        right[k + 1][j]
                    )
                else:
                    left_best = 0 if k == i else left[i][k - 1]
                    right_best = 0 if k == j else right[k + 1][j]

                    dp[i][j] = max(
                        left_best,
                        right_best
                    )

                left[i][j] = max(
                    left[i][j - 1],
                    total + dp[i][j]
                )

                right[i][j] = max(
                    right[i + 1][j],
                    total + dp[i][j]
                )

        return dp[0][n - 1]