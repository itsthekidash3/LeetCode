class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minimumcap = float('inf')
        minIndex = -1

        for i in range(len(capacity)):
            if itemSize <= capacity[i]:
                if capacity[i] < minimumcap:
                    minimumcap = capacity[i]
                    minIndex = i
        return minIndex
        