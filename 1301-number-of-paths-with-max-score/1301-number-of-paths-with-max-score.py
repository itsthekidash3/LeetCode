class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [-1] * (n + 1)
        ways = [0] * (n + 1)

        for r in range(n - 1, -1, -1):
            new_score = [-1] * (n + 1)
            new_ways = [0] * (n + 1)

            for c in range(n - 1, -1, -1):
                if board[r][c] == "X":
                    continue

                if board[r][c] == "S":
                    new_score[c] = 0
                    new_ways[c] = 1
                    continue

                best = max(score[c], new_score[c + 1], score[c + 1])

                if best == -1:
                    continue

                cnt = 0

                if score[c] == best:
                    cnt += ways[c]
                if new_score[c + 1] == best:
                    cnt += new_ways[c + 1]
                if score[c + 1] == best:
                    cnt += ways[c + 1]

                val = 0 if board[r][c] == "E" else int(board[r][c])

                new_score[c] = best + val
                new_ways[c] = cnt % MOD

            score = new_score
            ways = new_ways

        if score[0] == -1:
            return [0, 0]

        return [score[0], ways[0]]