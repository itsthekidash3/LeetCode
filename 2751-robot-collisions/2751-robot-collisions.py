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