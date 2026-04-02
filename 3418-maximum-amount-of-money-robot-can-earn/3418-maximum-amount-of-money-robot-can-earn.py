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

        R, C = len(coins), len(coins[0])
        store = [[-int(1e8)] * 3 for _ in range(C)]
        store[0] = [0, 0, 0]
        
        for i in range(R):
            for j in range(C):
                up = store[j]
                left = store[j - 1] if j != 0 else [-int(1e8)] * 3
                val = coins[i][j]

                store[j][0] = max(up[0] + val, left[0] + val, up[1], left[1])
                store[j][1] = max(up[1] + val, left[1] + val, up[2], left[2])
                store[j][2] = max(up[2] + coins[i][j], left[2] + coins[i][j])
        return max(store[C - 1])