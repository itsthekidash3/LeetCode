from collections import defaultdict
from functools import cache
import heapq
from math import inf

class Solution:
    def minimumCost(self, source, target, original, changed, cost):

        adj = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            adj[o].append((w, c))

        @cache
        def dijkstra(start, end):
            pq = [(0, start)]
            dist = defaultdict(lambda: inf)
            dist[start] = 0

            while pq:
                cur_cost, node = heapq.heappop(pq)
                if cur_cost > dist[node]:
                    continue

                for w, nxt in adj[node]:
                    new_cost = cur_cost + w
                    if new_cost < dist[nxt]:
                        dist[nxt] = new_cost
                        heapq.heappush(pq, (new_cost, nxt))

            return dist[end] if dist[end] != inf else -1

        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            c = dijkstra(s, t)
            if c == -1:
                return -1
            ans += c

        return ans
