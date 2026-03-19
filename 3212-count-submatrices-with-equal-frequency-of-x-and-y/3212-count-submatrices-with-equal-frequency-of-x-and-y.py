class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        px = [0] * n
        py = [0] * n

        for i in range(m):
            rowX = 0
            rowY = 0

            for j in range(n):
                if grid[i][j] == 'X':
                    rowX += 1
                elif grid[i][j] == 'Y':
                    rowY += 1

                px[j] += rowX
                py[j] += rowY

                if px[j] == py[j] and px[j] > 0:
                    ans += 1

        return ans