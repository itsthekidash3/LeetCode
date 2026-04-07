# took help of tarun sharma solution
class Robot:
    def __init__(self, width: int, height: int):
        # Goal: Initialize robot at origin facing East on a width × height grid
        # Grid boundaries: (0,0) to (width-1, height-1)
        
        self.x = 0          # Starting x-coordinate (leftmost)
        self.y = 0          # Starting y-coordinate (bottom)
        self.dir = "East"   # Initial direction
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        # Goal: Move robot num steps along grid perimeter (clockwise)
        # Approach: Calculate perimeter, use modulo to avoid redundant loops,
        # then move direction by direction until steps exhausted
        
        # Step 1: Calculate perimeter (robot walks along edges)
        # Perimeter = 2*(width-1) + 2*(height-1) because we count corners once
        perim = 2 * (self.width - 1) + 2 * (self.height - 1)
        
        # Step 2: Optimize using modulo (walking full perimeter returns to same spot)
        num %= perim
        if num == 0:
            num = perim  # If multiple of perimeter, walk full loop to reset to origin facing East
        
        # Step 3: Process movement direction by direction
        while num > 0:
            if self.dir == "East":
                # Moving right along bottom edge
                maxX = min(self.x + num, self.width - 1)  # Can't exceed right boundary
                rem = num - (maxX - self.x)  # Remaining steps after hitting boundary
                num = rem
                
                if rem == 0:  # Used all steps, stop here
                    self.x = maxX
                else:  # Hit right boundary, turn North (clockwise)
                    self.x = maxX
                    self.dir = "North"
            
            elif self.dir == "West":
                # Moving left along top edge
                minX = max(self.x - num, 0)  # Can't go below left boundary
                rem = num - (self.x - minX)  # Remaining steps after hitting boundary
                num = rem
                
                if rem == 0:  # Used all steps, stop here
                    self.x = minX
                else:  # Hit left boundary, turn South (clockwise)
                    self.x = minX
                    self.dir = "South"
            
            elif self.dir == "North":
                # Moving up along right edge
                maxY = min(self.y + num, self.height - 1)  # Can't exceed top boundary
                rem = num - (maxY - self.y)  # Remaining steps after hitting boundary
                num = rem
                
                if rem == 0:  # Used all steps, stop here
                    self.y = maxY
                else:  # Hit top boundary, turn West (clockwise)
                    self.y = maxY
                    self.dir = "West"
            
            elif self.dir == "South":
                # Moving down along left edge
                minY = max(self.y - num, 0)  # Can't go below bottom boundary
                rem = num - (self.y - minY)  # Remaining steps after hitting boundary
                num = rem
                
                if rem == 0:  # Used all steps, stop here
                    self.y = minY
                else:  # Hit bottom boundary, turn East (clockwise)
                    self.y = minY
                    self.dir = "East"

    def getPos(self):
        # Return current position as [x, y]
        return [self.x, self.y]
    
    def getDir(self):
        # Return current direction as string
        return self.dir