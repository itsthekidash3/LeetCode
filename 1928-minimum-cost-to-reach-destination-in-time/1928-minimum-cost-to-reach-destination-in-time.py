class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        # This is NOT standard Dijkstra.
        # We minimize COST, but are constrained by TIME.
        # Same city can be visited multiple times with different (time, cost).

        from collections import defaultdict
        import heapq
        import math

        # Build adjacency list: city -> (neighbor, travel_time)
        Travel = defaultdict(list)
        for city1, city2, time in edges:
            Travel[city1].append((city2, time))
            Travel[city2].append((city1, time))

        n = len(passingFees)

        # cost[i] = minimum cost found so far to reach city i
        # time[i] = minimum time found so far to reach city i
        cost = [math.inf] * n
        time = [math.inf] * n

        # Heap state:
        # (total_cost_so_far, total_time_so_far, current_city)
        heap = [(passingFees[0], 0, 0)]

        while heap:
            currCost, currTime, city = heapq.heappop(heap)

            # If time exceeds maxTime, this path is invalid
            if currTime > maxTime:
                continue

            # IMPORTANT PRUNING RULE:
            # If we have already reached this city with BOTH:
            # - lower or equal cost
            # - lower or equal time
            # then this state is dominated and useless
            if cost[city] <= currCost and time[city] <= currTime:
                continue

            # Record the best known values for this city
            cost[city] = currCost
            time[city] = currTime

            # If destination reached, this is the minimum cost
            # because heap is ordered by cost
            if city == n - 1:
                return currCost

            # Relax edges
            for nextCity, travelTime in Travel[city]:
                newTime = currTime + travelTime
                newCost = currCost + passingFees[nextCity]

                # Push new state into heap
                # We do NOT immediately prune based on time or cost alone
                heapq.heappush(heap, (newCost, newTime, nextCity))

        return -1
