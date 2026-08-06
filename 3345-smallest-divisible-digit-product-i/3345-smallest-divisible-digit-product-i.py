class Solution:
    def productOfDigits(self, n: int) -> int:
        product = 1
        while n > 0:
            product *= n % 10
            n //= 10
        return product

    def smallestNumber(self, n: int, t: int) -> int:
        while self.productOfDigits(n) % t != 0:
            n += 1
        return n