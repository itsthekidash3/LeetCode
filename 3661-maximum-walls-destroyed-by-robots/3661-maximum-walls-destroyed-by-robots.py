# borrowed code from larry for a better understanding

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # how many walls destroyed
        # bullet travels left or right
        # robot at ith position and fixed
        # bullet travels distance[i]
        # wall is at position j in walls[j]
        # robot has one bullet each
        # bullet travels left or right
        # bullet hits robot , stops
        # bullet destroys every wall in its path within the distamce[i] range
        # number line of the row?
        #need to return the "Unique" walls hit

        # robot within firing range?
        #  if yes how many walls hit before reaching the robot

        # dp with preprocessing
        # dp determining the length of the line
        # previous_left -> last index shot to the right: what are we position the left respevtive of?
        # sort the robot by location
        # communicate
        N = len(robots)
        r = []
        for rx,rd in zip(robots,distance):
            r.append((rx,rd)) # (robot_position, bullet_distance)
        r.sort() # sorting the robots by position with the bullet distance
        sl = SortedList(walls) # sorting the walls


        def c(left,right): # binary search : Count walls in range [left, right] using binary search
            lindex = sl.bisect_left(left) # First wall >= left
            rindex = sl.bisect_right(right) # First wall > right
            return rindex - lindex # Number of walls in range

        @cache

        # two binary search to get the no of walls in position
        # index -> N -> of the robot
        # boundary -> 2 things only
        #       previous robot location 
        #       previous robot location + 1
        def f(index,boundary):
            if index == N:
                return 0
            
            # shoot left or shoot right
            # you have to shoot it : ask question

            # shoot right
            # we shoot from x to x + d

            right = r[index][0] + r[index][1] # index = robot position on the line , distance : bullet distance still at same robot btw
                                                # [index][0] = position of the robot, [index][1] = distance of the bullet
                                                # r = ([robot position][distance of the bullet]) , at index : the robot number after sorting
            if index + 1 < N:
                right = min(right, r[index+1][0] - 1)
            best = f(index + 1,right + 1) +  c(r[index][0], right)  # no of things that get shot, double counting things

            # shoot left
            # the boundary doesnot matter
            # we assume that the boudary stops at the current index 
            # we shot from x to x-d

            left = r[index][0] - r[index][1]
            # Bullet can't go past boundary (area already covered by previous robot)
            if index - 1 >= 0:
                left = max(left, boundary) # Respect boundary to avoid double-counting

            # Walls hit shooting left + recurse with updated boundary
            # New boundary = current robot position + 1 (next robot shooting left stops here)
            
            best = max(best, f(index + 1, r[index][0] + 1) + c(left,r[index][0]))

            return best
        
        return f(0,-1)





        
        