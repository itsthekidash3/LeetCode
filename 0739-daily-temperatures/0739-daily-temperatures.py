class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # APPROACH: Monotonic Decreasing Stack
        # - Stack holds [temp, index] pairs in decreasing order of temperature
        # - For each new temp, if it's warmer than the top of the stack, that top has found its answer
        # - Pop everything cooler than current temp, recording the index difference as the wait days
        # - If we never find a warmer day, the default 0 in res handles it (initialized at the start)
        # - Brute force is O(n^2); this is O(n) since each element is pushed and popped at most once

        res = [0] * len(temperatures)  # default 0 for days that never get a warmer day
        stack = []  # monotonic decreasing stack of [temp, index] pairs

        for i, t in enumerate(temperatures):
            # pop everything cooler than current temp — current day is their answer
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex  # days waited = index difference
            stack.append([t, i])  # current temp hasn't found a warmer day yet, hold it

        return res  # anything left in stack stays 0 — no warmer day ever came