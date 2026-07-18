class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        return self.gcd(mn, mx)