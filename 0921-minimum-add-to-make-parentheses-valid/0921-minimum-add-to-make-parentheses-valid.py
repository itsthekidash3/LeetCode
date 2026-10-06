class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        result = 0

        for ch in s:
            if ch == '(':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    result += 1

        return result + count