class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # how do i use sliding window in this?
        # maximum length of a substring in a array?

        setChar = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in setChar:
                setChar.remove(s[l])
                l += 1
            setChar.add(s[r])
            result = max(result, r-l+1)
        
        return result
        