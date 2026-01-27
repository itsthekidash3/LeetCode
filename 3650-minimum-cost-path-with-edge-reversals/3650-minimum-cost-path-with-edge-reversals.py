class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        """
        We want the minimum cost to go from node 0 to node n-1.

        Each edge (u -> v) has:
        - cost = w if we go u -> v
        - cost = 2w if we go v -> u (reverse direction)

        This becomes a standard shortest-path problem on a weighted graph,
        which we solve using Dijkstra’s algorithm.
        """

        from collections import defaultdict
        import heapq
        import math

        # ----------------------------------------------------
        # STEP 1: Build an augmented adjacency list
        # ----------------------------------------------------
        # adj[u] = list of (v, cost) pairs
        #
        # For each original edge (u, v, w):
        #   - add u -> v with cost w
        #   - add v -> u with cost 2w
        #
        # This way, Dijkstra does not need to know about
        # "direction rules" — they are baked into the graph.
        # ----------------------------------------------------

        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))        # forward direction
            adj[v].append((u, 2 * w))    # reverse direction (penalty)

        # ----------------------------------------------------
        # STEP 2: Dijkstra initialization
        # ----------------------------------------------------
        # dist[x] = minimum cost to reach node x from node 0
        #
        # Initialize all distances to infinity
        # except dist[0] = 0 (starting point)
        # ----------------------------------------------------

        dist = [math.inf] * n
        dist[0] = 0

        # Min-heap storing (current_distance, node)
        heap = [(0, 0)]

        # ----------------------------------------------------
        # STEP 3: Dijkstra main loop
        # ----------------------------------------------------
        while heap:
            d, u = heapq.heappop(heap)

            # If we reached the destination node,
            # we can return immediately because Dijkstra
            # guarantees this is the minimum cost.
            if u == n - 1:
                return d

            # If this entry is stale (not the best known distance),
            # skip it
            if d != dist[u]:
                continue

            # Relax edges going out of u
            for v, w in adj[u]:
                new_cost = dist[u] + w

                if dist[v] > new_cost:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

        # If node n-1 is unreachable
        return -1
