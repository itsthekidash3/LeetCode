class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        # STRATEGY: Binary search on the answer (time in seconds)
        # For a given time limit, check if workers can reduce mountain to 0
        
        # KEY INSIGHT: For worker with time t, to reduce height by x units:
        # Total time = t*1 + t*2 + t*3 + ... + t*x = t * (1+2+...+x) = t * x*(x+1)/2
        # Given time limit T, max units worker can reduce: solve T = t * x*(x+1)/2
        # Rearranging: x^2 + x - 2T/t = 0
        # Using quadratic formula: x = (-1 + sqrt(1 + 8T/t)) / 2
        
        lo, hi = 1, 10**16  # Binary search bounds on time
        
        while lo < hi:
            mid = (lo + hi) >> 1  # Same as (lo + hi) // 2, but faster
            tot = 0  # Total height reduction possible in 'mid' seconds
            
            # For each worker, calculate how much height they can reduce in 'mid' seconds
            for t in workerTimes:
                # Solve: mid = t * x*(x+1)/2 for x
                # x^2 + x - 2*mid/t = 0
                # x = (-1 + sqrt(1 + 8*mid/t)) / 2
                # Rewritten: sqrt(2*mid/t + 0.25) - 0.5
                # The formula: sqrt(mid/t * 2 + 0.25) - 0.5 gives max units this worker can reduce
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                
                # Early exit optimization: if we already have enough, stop checking
                if tot >= mountainHeight: 
                    break
            
            # Binary search logic: adjust bounds based on feasibility
            if tot >= mountainHeight:
                hi = mid  # 'mid' seconds is enough, try smaller
            else:
                lo = mid + 1  # 'mid' seconds not enough, need more time
        
        return lo  # Minimum time needed