class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt, ans, used = 0, [], 0
        for a, b in zip(A, B):
            cnt += (used >> a) & 1
            used |= 1 << a
            cnt += (used >> b) & 1
            used |= 1 << b
            ans.append(cnt)
        return ans