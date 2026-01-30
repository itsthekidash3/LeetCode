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
        N = len(original)
        adj = defaultdict(list)
        for i in range(N):
            adj[original[i]].append((cost[i], changed[i]))

        @cache
        def get_cost(start: str, end: str) -> int:
            """
            Returns minimum cost to convert character `start` to `end`
            using Dijkstra. Returns -1 if impossible.
            """
            pq = [(0, start)]           # (current_cost, node)
            dist = defaultdict(lambda: inf)
            dist[start] = 0

            while pq:
                cost, node = heapq.heappop(pq)

                # Skip stale states
                if cost > dist[node]:
                    continue

                # Found cheapest path to end
                if node == end:
                    return cost

                # Relax edges
                for next_cost, next_node in adj[node]: 
                    if cost + next_cost < dist[next_node]: 
                        dist[next_node] = cost + next_cost 
                        heapq.heappush(pq, (dist[next_node], next_node))

            return -1  # end not reachable

        # Total cost to convert source -> target
        ans = 0 
        for start, end in zip(source, target): 
            if start == end: continue 
            cost = get_cost(start, end) 
            if cost == -1: return -1 
            ans += cost 

        return ans



        