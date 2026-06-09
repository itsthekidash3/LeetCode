class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        self.enc = encCost
        self.flat = flatCost

        n = len(s)
        self.pref = [0] * (n + 1)

        for i in range(n):
            self.pref[i + 1] = self.pref[i] + (1 if s[i] == '1' else 0)

        return self.solve(0, n - 1)

    def solve(self, l: int, r: int) -> int:
        length = r - l + 1
        ones = self.pref[r + 1] - self.pref[l]

        direct = self.flat if ones == 0 else length * ones * self.enc

        if length % 2 == 1:
            return direct

        mid = (l + r) // 2
        split = self.solve(l, mid) + self.solve(mid + 1, r)

        return min(direct, split)