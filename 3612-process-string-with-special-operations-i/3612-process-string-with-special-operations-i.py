class Solution:
    def processStr(self, s: str) -> str:
        ans = ""

        for c in s:
            if 'a' <= c <= 'z':
                ans += c
            elif c == '*':  # remove one char
                if ans:
                    ans = ans[:-1]
            elif c == '#':  # duplicate
                ans += ans
            else:  # '%'
                ans = ans[::-1]

        return ans