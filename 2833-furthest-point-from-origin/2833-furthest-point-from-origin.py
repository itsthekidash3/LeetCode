class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # ✨ One-liner version (3 passes, super clean):
        # return abs(moves.count('L') - moves.count('R')) + moves.count('_')

        # 🔁 One-pass version (1 pass, more explicit):
        L = R = Dash = 0
        for i in moves:
            if i == "L":
                L += 1
            elif i == "R":
                R += 1
            else:
                Dash += 1
        return abs(L - R) + Dash

# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [April 07, 2026]