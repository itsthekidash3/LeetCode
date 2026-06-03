# ============================================================
# LeetCode 3633 — Earliest Finish Time for Land and Water Rides I
# (also applies to 3635 — Rides II, same algorithm)
#
# Approach: Greedy Enumeration over Two Orderings
#
# Time Complexity:  O(n + m)  — one pass over each ride list
# Space Complexity: O(1)      — only scalar trackers, no aux structures
#
# Core Insight:
#   You must ride exactly one land ride AND one water ride (in some order).
#   The only two valid orderings are Land→Water or Water→Land.
#   For each ordering, greedily pick the first-type ride that ends earliest,
#   then find the second-type ride that finishes soonest given that constraint.
# ============================================================

class Solution:

    def calFinishTime(self, ls, ld, ws, wd):
        # ─────────────────────────────────────────────────────────
        # ROLE: Compute the best finish time assuming we do an
        #       "ls/ld" ride FIRST, then an "ws/wd" ride SECOND.
        #
        # Parameters (short names used for generality — called both ways):
        #   ls = first-type start times,    ld = first-type durations
        #   ws = second-type start times,   wd = second-type durations
        # ─────────────────────────────────────────────────────────

        mini = float('inf')

        # ── PHASE 1: Find the earliest we can be done with the FIRST ride ──
        #
        # Trace (ls=[5,3], ld=[3,6]):
        #   i=0 → 5+3=8,  mini=8
        #   i=1 → 3+6=9,  mini stays 8
        # → mini = 8  (we finish the first ride no later than time 8)
        #
        # WHY: We get to choose which first-type ride to take.
        #      We want the one with the smallest finish time = start + duration.
        #      This is our "handoff time" — when we're free to start the second ride.
        for i in range(len(ls)):
            mini = min(mini, ls[i] + ld[i])

        ans = float('inf')

        # ── PHASE 2: Over all second-type rides, find the one that finishes earliest ──
        #
        # Trace (ws=[1,8], wd=[10,6], mini=8):
        #   i=0 → max(8,1)=8,  8+10=18
        #   i=1 → max(8,8)=8,  8+6=14  ← ans=14
        # → ans = 14
        #
        # WHY max(mini, ws[i])?
        #   We can only START the second ride once BOTH conditions are met:
        #     (a) the first ride is done       → at time `mini`
        #     (b) this second ride has opened  → at time `ws[i]`
        #   We have to wait for whichever is later. Then we ride for wd[i].
        for i in range(len(ws)):
            ans = min(
                ans,
                max(mini, ws[i]) + wd[i]
            )
            # → tracks the global minimum finish time across all second-ride choices

        return ans

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        # Edge case: the problem guarantees non-empty lists and valid times,
        # but the float('inf') sentinels in calFinishTime handle degenerate inputs safely.

        # Try BOTH valid orderings and return the overall best:
        #
        #   Option A: Land ride first, then Water ride
        #   Option B: Water ride first, then Land ride
        #
        # WHY both? The ride that ends earliest as "first" depends on the schedule,
        # and the optimal second ride depends on which type you did first.
        # There's no way to know which ordering wins without checking both.
        return min(
            self.calFinishTime(landStartTime, landDuration, waterStartTime, waterDuration),  # Land → Water
            self.calFinishTime(waterStartTime, waterDuration, landStartTime, landDuration)   # Water → Land
        )