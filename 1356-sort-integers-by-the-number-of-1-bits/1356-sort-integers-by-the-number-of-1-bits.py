class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # bit manipulation
        # how to do bit manipulation?
        # right shift or should i convert to a number ?
        # 
        return sorted(arr, key = lambda x: (x.bit_count(), x))

        # sorted() returns a new sorted list of arr
    # key = tells sorted() HOW to score/compare each element
    # lambda x: means "for each number x in arr, return this score..."
    # (x.bit_count(), x) is the score — a tuple of (number of 1-bits, the number itself)
    # Python sorts by the first value in the tuple, and uses the second to break ties   