class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        events = [(v,i) for i,v in enumerate(positions)] # store the position and value
        events.sort() # can also use zip function
        # coding is the fun part . logic is the one you have to get. not solution the intuiton and think if edge cases
        # naming in the way it makes sense to a human being
        # bfs or deque approach
        st = [] # use stack

        for val, indx in events:
            if directions[indx] == 'R': # direction of robot at thay position
                st.append(indx)
            else:
                while st and (directions[st[-1]]) == 'R' and healths[st[-1]] < healths[indx]: # same direction
                    healths[st.pop()] = 0
                    healths[indx] -= 1
                if healths[indx] == 0: # no health
                    continue
                elif not st or directions[st[-1]] == 'L': # different direction
                    st.append(indx)
                elif healths[indx]==healths[st[-1]]: # pop both if same health
                    healths[indx] = 0
                    healths[st.pop()] = 0
                else:
                    healths[indx] = 0
                    healths[st[-1]] -= 1
        ans = [t for t in healths if t > 0]
        return ans

# ALTERNATIVE DEQUE SOLUTION:
# 
# class Solution:
#     def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#         # Create queue of (position, health, direction, robot_id) sorted by position
#         # robot_id tracks original order (1-indexed here)
#         q = deque(sorted([
#             (pos, h, d, rid + 1) for rid, (pos, h, d) in enumerate(zip(positions, healths, directions))
#         ]))
#         
#         robots = []  # Stores survivors
#         
#         while q:
#             pos, h, d, rid = q.popleft()
#             
#             # Left-moving robot: no future collisions, immediately survives
#             if d == 'L':
#                 robots.append((pos, h, d, rid))
#                 continue
#             
#             # Right-moving robot: check for collisions with upcoming left-movers
#             if not q:
#                 robots.append((pos, h, d, rid))
#                 continue
#             
#             while q:
#                 nepos, neh, ned, nerid = q.popleft()
#                 
#                 # Next robot also moving right: current survives, process next
#                 if ned == 'R':
#                     robots.append((pos, h, d, rid))
#                     pos, h, d, rid = nepos, neh, ned, nerid
#                     if not q:
#                         robots.append((pos, h, d, rid))
#                     continue
#                 
#                 # Collision! Current 'R' vs next 'L'
#                 if h == neh:
#                     # Equal health: both die, reprocess last survivor if exists
#                     if robots:
#                         prev = robots.pop()
#                         q.appendleft(prev)
#                     break
#                 elif h > neh:
#                     # Right robot wins, loses 1 health, continues fighting
#                     h -= 1
#                     if not q:
#                         robots.append((pos, h, d, rid))
#                     continue
#                 else:
#                     # Left robot wins, loses 1 health, reinsert to fight previous survivors
#                     q.appendleft((nepos, neh - 1, ned, nerid))
#                     if robots:
#                         prev = robots.pop()
#                         q.appendleft(prev)
#                     break
#         
#         # Return healths sorted by original robot_id
#         return [h for pos, h, d, rid in sorted(robots, key=lambda r: r[3])]