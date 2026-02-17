class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setChar = set()  # stores unique characters in current window
        l = 0            # left pointer of the sliding window
        result = 0       # tracks the longest substring found so far

        for r in range(len(s)):         # expand window by moving right pointer
            while s[r] in setChar:      # if duplicate found, shrink from the left
                setChar.remove(s[l])    # remove leftmost character
                l += 1                  # move left pointer forward

            setChar.add(s[r])           # add new character to the window
            result = max(result, r - l + 1)  # update result if current window is larger

        return result
        