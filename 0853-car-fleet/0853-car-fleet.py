class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # APPROACH: Stack + Sorting by position (right to left)
        # - Pair each car's position and speed together, then sort right to left
        #   (closest to target first) so we can simulate cars catching up naturally
        # - Calculate time for each car to reach target: (target - p) / s
        # - If a car behind takes LESS or EQUAL time than the car ahead, it catches up → same fleet, pop it
        # - If it takes MORE time, it can never catch up → new fleet, keep it on stack
        # - Each element on the stack at the end = a distinct fleet
        # - O(nlogn) due to sorting

        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []  # each entry = arrival time of a fleet leader

        for p, s in sorted(pair)[::-1]:  # process cars from closest to target → furthest
            stack.append((target - p) / s)  # time this car takes to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # caught up to the car ahead
                stack.pop()  # merges into the fleet ahead, discard the faster time

        return len(stack)  # remaining entries = distinct fleets that never merged