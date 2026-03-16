# borrowed code from vkram4 to get a better understanding !

class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])

        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        top3 = set()

        def add_value(val):
            top3.add(val)
            if len(top3) > 3:
                top3.remove(min(top3))

        for i in range(m):
            for j in range(n):
                add_value(grid[i][j])

                k = 1
                while i - k >= 0 and i + k < m and j - k >= 0 and j + k < n:
                    topR, topC = i - k, j
                    rightR, rightC = i, j + k
                    bottomR, bottomC = i + k, j
                    leftR, leftC = i, j - k

                    border = 0

                    # top -> right   (\)
                    border += diag1[rightR + 1][rightC + 1] - diag1[topR][topC]

                    # right -> bottom (/)
                    border += diag2[bottomR + 1][bottomC] - diag2[rightR][rightC + 1]

                    # left -> bottom  (\)
                    border += diag1[bottomR + 1][bottomC + 1] - diag1[leftR][leftC]

                    # top -> left     (/)
                    border += diag2[leftR + 1][leftC] - diag2[topR][topC + 1]

                    # corners counted twice
                    border -= grid[topR][topC]
                    border -= grid[rightR][rightC]
                    border -= grid[bottomR][bottomC]
                    border -= grid[leftR][leftC]

                    add_value(border)
                    k += 1

        return sorted(top3, reverse=True)