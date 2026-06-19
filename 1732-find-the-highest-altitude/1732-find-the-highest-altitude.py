class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0
        for x in gain:
            current += x
            highest = max(highest, current)
        return highest
    