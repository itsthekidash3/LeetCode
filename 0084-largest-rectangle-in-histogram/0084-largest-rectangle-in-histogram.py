class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # APPROACH: Monotonic Increasing Stack
        # - Stack holds (index, height) pairs in increasing order of height
        # - A bar can extend LEFT as far back as the last bar that was taller than it (got popped)
        # - When we hit a bar shorter than the stack top, the top can no longer extend right → compute its area
        # - The trick: when popping, carry the start index backwards — the shorter current bar
        #   can extend all the way back to where the popped bar started
        # - Anything left in the stack at the end can extend all the way to the right edge

        maxArea = 0
        stack = []  # monotonic increasing stack of (start_index, height)

        for i, h in enumerate(heights):
            start = i  # assume we can only start here, may extend backwards if we pop
            while stack and stack[-1][1] > h:  # current bar is shorter → pop taller bars
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))  # width = how far right it could reach
                start = index  # current bar can now extend back to where the popped bar started
            stack.append((start, h))  # push with (possibly extended) start index

        # bars still in stack were never blocked → they extend all the way to the right edge
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea