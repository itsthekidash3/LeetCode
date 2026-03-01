class Solution:
    def minPartitions(self, n: str) -> int:
        # APPROACH: Find the largest digit
        # - each deci-binary number can only contribute AT MOST 1 to each digit position
        # - think of stacking deci-binary numbers in columns — each column grows by 1 per number
        # - the largest digit is the bottleneck: it needs that many 1s stacked in its column
        # - every other digit can be satisfied within that same count
        # - so the answer is simply the largest digit in the entire string

        best = 0
        for c in n:
            best = max(best, int(c))  # largest digit seen so far = minimum numbers needed

        return best  # the bottleneck digit determines the whole answer