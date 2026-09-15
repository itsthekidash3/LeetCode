class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        N, ans, start = len(S), 0, 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= start and right < N and S[left] == S[right]:
                if right + 1 - left >= k: 
                    ans += 1
                    start = right + 1
                    break
                left -= 1
                right += 1
        return ans
        