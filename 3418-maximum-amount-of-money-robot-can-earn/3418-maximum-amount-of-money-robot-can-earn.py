# borrowed code from indean condor for better understanding

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # dp - DFS 
        # fight against top two negative
        # its a given

        # have to see the path that i have to take and neutralize the robber
        # top - down approach

        # when do you neutalize ? two negative or 
        # acess a different cells
        # take three states
        #For each coin in the current row, there are three possibilities:
        # The coin is used with no previous coin, or
        # The coin is used with a previous coin, or
        # The coin is used while keeping track of coins collected in previous rows.   
        # 3d matrix with row,col and k being the neutrazliztion
        # basic dp approach

        R, C = len(coins), len(coins[0])
        # store[j][k] = max coins we can collect ending at column j with k neutralizations used
        store = [[-int(1e8)] * 3 for _ in range(C)]
        store[0] = [0, 0, 0]  # Starting state: no coins collected, 0/1/2 neutralizations available
        
        for i in range(R):
            for j in range(C):
                up = store[j]  # State from cell above (previous row, same column)
                left = store[j - 1] if j != 0 else [-int(1e8)] * 3  # State from left cell
                val = coins[i][j]
                
                # Update state with k neutralizations used:
                # Option 1: Take current coin (add val from prev state with k neutralizations)
                # Option 2: Neutralize current coin (transition from prev state with k-1 neutralizations)
                store[j][0] = max(up[0] + val, left[0] + val, up[1], left[1])  # 0 neutralizations used
                store[j][1] = max(up[1] + val, left[1] + val, up[2], left[2])  # 1 neutralization used
                store[j][2] = max(up[2] + val, left[2] + val)  # 2 neutralizations used (all exhausted)
        
        return max(store[C - 1])  # Max among all neutralization states at bottom-right