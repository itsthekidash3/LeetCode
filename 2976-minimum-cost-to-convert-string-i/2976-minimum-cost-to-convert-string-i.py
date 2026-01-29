class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        # source : string same length
        # target : string
        # original : character array
        # changed : character array
        # cost : integer array  - to change from original to changed
        # In one operation, you can pick a character x from the string and change it to the character y at a cost of z 
        # if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y - it should be at that index
        # there can be duplicates as well

        "abcd"    "acbe"
        # original = ["a","b","c","c","e","d"]
        # changed = ["b","c","b","e","b","e"]
        # cost = [2,5,5,1,2,20]

        # does index matter if i store the key : value pair as original[i] : changed[i],cost[i]
        # or should i store as cost[i] : original[i], changed[i]
        # was able to arrive at the idea, but implemntatoion was hard to figure out

         # Build adjacency list:
        # adj[u] = list of (weight, v)
        adj = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            adj[o].append((w, c))

        @cache
        def dijkstra(start: str, end: str) -> int:
            """
            Returns minimum cost to convert character `start` to `end`
            using Dijkstra. Returns -1 if impossible.
            """
            pq = [(0, start)]           # (current_cost, node)
            dist = defaultdict(lambda: inf)
            dist[start] = 0

            while pq:
                cur_cost, node = heapq.heappop(pq)

                # Skip stale states
                if cur_cost > dist[node]:
                    continue

                # Found cheapest path to end
                if node == end:
                    return cur_cost

                # Relax edges
                for edge_cost, nxt in adj[node]:
                    new_cost = cur_cost + edge_cost
                    if new_cost < dist[nxt]:
                        dist[nxt] = new_cost
                        heapq.heappush(pq, (new_cost, nxt))

            return -1  # end not reachable

        # Total cost to convert source -> target
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            c = dijkstra(s, t)
            if c == -1:
                return -1
            total += c

        return total




        