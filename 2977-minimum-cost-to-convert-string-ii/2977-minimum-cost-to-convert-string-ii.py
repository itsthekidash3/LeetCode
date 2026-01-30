import heapq
from collections import defaultdict
from functools import cache
from typing import List

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        """
        Core idea:
        - Use a GRAPH + DIJKSTRA to find the cheapest way to convert one string -> another
        - Use DP to decide WHERE to apply those conversions on the source string
        """

        n = len(source)          # length of source / target
        m = len(cost)            # number of conversion rules
        inf = 10**20

        # ------------------------------------------------------------
        # 1. Build graph: original[i] -> changed[i] with cost[i]
        # ------------------------------------------------------------
        g = defaultdict(list)
        for i in range(m):
            g[original[i]].append((changed[i], cost[i]))

        # ------------------------------------------------------------
        # 2. Dijkstra:
        #    minimum cost to convert string sc -> string t
        # ------------------------------------------------------------
        @cache
        def dijk(sc, t):
            """
            Standard Dijkstra on string-graph.
            Nodes = strings
            Edges = allowed conversions with costs
            """
            dist = defaultdict(lambda: inf)
            pq = []

            dist[sc] = 0
            heapq.heappush(pq, (0, sc))

            while pq:
                cur_cost, node = heapq.heappop(pq)

                if cur_cost > dist[node]:
                    continue

                if node == t:
                    return cur_cost

                for nxt, w in g[node]:
                    if dist[nxt] > cur_cost + w:
                        dist[nxt] = cur_cost + w
                        heapq.heappush(pq, (dist[nxt], nxt))

            return inf  # unreachable

        # ------------------------------------------------------------
        # 3. DP:
        #    rec(i) = minimum cost to convert source[i:] -> target[i:]
        # ------------------------------------------------------------
        @cache
        def rec(i):
            # If we passed the end -> invalid
            if i > n:
                return inf

            # If we exactly finished the string -> no cost left
            if i == n:
                return 0

            ans = inf

            # --------------------------------------------------------
            # Try applying every conversion rule starting at index i
            # --------------------------------------------------------
            for k in range(m):
                l = len(original[k])  # length of the substring we want to replace

                # Make sure substring fits inside source
                if i + l <= n:
                    # Check if source substring matches this rule
                    if source[i:i+l] == original[k]:
                        # Cost =
                        # 1) cost to convert this substring to target[i:i+l]
                        # 2) + optimal cost to finish the rest (rec(i+l))
                        ans = min(
                            ans,
                            dijk(original[k], target[i:i+l]) + rec(i+l)
                        )

            # --------------------------------------------------------
            # Option: do nothing at this index if characters already match
            # --------------------------------------------------------
            if source[i] == target[i]:
                ans = min(ans, rec(i + 1))

            return ans

        # ------------------------------------------------------------
        # Start DP from index 0
        # ------------------------------------------------------------
        res = rec(0)
        rec.cache_clear()

        return res if res < inf else -1
