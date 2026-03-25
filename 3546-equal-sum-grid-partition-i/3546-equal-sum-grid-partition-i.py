# used the hint a bit horizontal/vertical cut 🫠
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        r,c = len(grid), len(grid[0])

        # compare row sum and colum sum
        # colum sum matrix and row sum matrix
        # c1 sum, c2 sum, ....
        # tow pointers? 
        # vertical cut / horozpntal cut

        colSum = [0] * c
        rowSum = [0] * r

        for i in range(r):
            for j in range(c):
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]
        
        # do a horixontal cut i.e row cut

        total = sum(rowSum)
        count = 0

        for i in range(r):
            count += rowSum[i]
            if count == total - count:
                return True

        total = sum(colSum)
        count = 0

        for j in range(c):
            count += colSum[j]
            if count == total - count:
                return True
        
        return False




