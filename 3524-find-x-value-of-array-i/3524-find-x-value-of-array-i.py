class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0 for _ in range(k)]
        prev = [0 for _ in range(k)]
        for num in nums:
            numm = num % k
            curr = [0] * k
            curr[numm] += 1
            for r, cnt in enumerate(prev):
                if cnt:
                    curr[(r * numm) % k] += cnt
            for r in range(k):
                res[r] += curr[r]
            prev = curr
        return res