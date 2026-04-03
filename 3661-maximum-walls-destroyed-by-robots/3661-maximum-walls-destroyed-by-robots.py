from sortedcontainers import SortedList
from functools import lru_cache

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        N = len(robots)
        r = [(robots[i], distance[i]) for i in range(N)]
        r.sort()
        
        # Precompute reachable walls for each robot in each direction
        left_walls = []
        right_walls = []
        
        for i in range(N):
            pos, dist = r[i]
            
            # Right
            right_bound = pos + dist
            if i + 1 < N:
                right_bound = min(right_bound, r[i+1][0] - 1)
            right_walls.append(tuple(sorted([w for w in walls if pos <= w <= right_bound])))
            
            # Left
            left_bound = pos - dist
            if i - 1 >= 0:
                left_bound = max(left_bound, r[i-1][0] + 1)
            left_walls.append(tuple(sorted([w for w in walls if left_bound <= w <= pos])))
        
        @lru_cache(maxsize=None)
        def dp(index, destroyed_tuple):
            if index == N:
                return 0
            
            destroyed = set(destroyed_tuple)
            
            # Shoot right
            new_right = destroyed | set(right_walls[index])
            gain_right = len(set(right_walls[index]) - destroyed)
            result_right = gain_right + dp(index + 1, tuple(sorted(new_right)))
            
            # Shoot left  
            new_left = destroyed | set(left_walls[index])
            gain_left = len(set(left_walls[index]) - destroyed)
            result_left = gain_left + dp(index + 1, tuple(sorted(new_left)))
            
            return max(result_right, result_left)
        
        return dp(0, ())