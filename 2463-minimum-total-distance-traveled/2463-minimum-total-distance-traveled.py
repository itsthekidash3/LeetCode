# Borrowed code from Ajay Chiudary for better understanding

class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        # robot[i]
        # factory[j] = [positionj, limit]

        # at any moment set a direction, for some robots
        # minimize the dist travelled by all robots

        # how do we set the direction : minimum distcnace

        # minimum distance from robot to factory and the factory limit
        # keep track of limit and minimum distance
        # 0 <= limitj <= robot.length

        # greedy method

        # sort for 

        # Goal: Assign robots to factories minimizing total travel distance
        # Constraints: Each factory has limited capacity, each robot goes to one factory
        # Approach: DP with space optimization (2D → 1D using rolling arrays)
        
        # Step 1: Sort robots and factories by position for optimal assignment
        robots.sort()
        factories.sort()
        
        # Step 2: Flatten factory positions according to their capacities
        # Each factory with capacity k becomes k separate "slots" at that position
        factory_positions = []
        for factory in factories:
            position, capacity = factory[0], factory[1]
            for i in range(capacity):
                factory_positions.append(position)
        
        robot_count = len(robots)
        factory_count = len(factory_positions)
        
        # Step 3: Initialize DP arrays (space optimization: only keep 2 rows)
        # next_dist[j] = min distance for remaining robots when starting from factory j
        # current[j] = min distance being computed for current robot
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]
        
        # Base case: If we run out of factory slots, cost is infinite (impossible)
        current[factory_count] = 1e12
        
        # Step 4: Fill DP table bottom-up (process robots right to left)
        # dp[i][j] = min total distance to assign robots[i:] to factory_positions[j:]
        for i in range(robot_count - 1, -1, -1):  # For each robot (reverse order)
            for j in range(factory_count - 1, -1, -1):  # For each factory slot (reverse)
                
                # Option 1: Assign current robot to current factory slot
                # Cost = distance from robot[i] to factory[j] + optimal cost for remaining
                assign = (
                    abs(robots[i] - factory_positions[j]) + next_dist[j + 1]
                )
                
                # Option 2: Skip current factory slot (don't assign robot[i] here)
                # Try next factory slot for this robot
                skip = current[j + 1]
                
                # Take minimum of both options
                current[j] = min(assign, skip)
            
            # Move to next robot: current row becomes next_dist for previous robot
            next_dist = current[:]
        
        # Step 5: Return minimum distance starting from first robot and first factory
        return current[0]



        