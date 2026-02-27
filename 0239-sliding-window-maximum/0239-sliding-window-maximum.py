class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # APPROACH: Monotonic Decreasing Deque
        # - Deque stores INDICES (not values), ordered so their corresponding values are decreasing
        # - Front of deque always holds the index of the current window's maximum
        # - Before adding a new element, evict all indices whose values are smaller (they'll never be the max)
        # - Evict the front if it's slid out of the window's left boundary

        output = []
        q = collections.deque()  # monotonic decreasing deque of indices

        l = r = 0

        while r < len(nums):

            # Maintain decreasing order: pop from the back anything smaller than nums[r]
            # (those elements are useless — nums[r] is both newer and larger)
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)  # add current index to the back

            # Evict front if it's outside the window [l, r]
            if l > q[0]:
                q.popleft()

            # Only start recording results once the first full window is formed
            if (r + 1) >= k:
                output.append(nums[q[0]])  # q[0] is always the index of the window max
                l += 1  # slide the window forward

            r += 1

        return output