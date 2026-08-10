class Solution:
    MAX = 100000
    dp = [False] * (MAX + 1)

    for i in range(MAX + 1):
        if dp[i]:
            continue

        for j in range(1, int((MAX - i) ** 0.5) + 1):
            dp[i + j * j] = True

    def winnerSquareGame(self, n: int) -> bool:
        return self.dp[n]