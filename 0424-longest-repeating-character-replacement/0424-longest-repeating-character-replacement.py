class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}   # tracks frequency of each character in current window
        l = 0        # left pointer
        result = 0   # longest valid window found so far

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1   # add right character to frequency map if no entry return 0
        
            # if window size minus the most frequent character exceeds k,
            # we need more than k replacements to make the window uniform — shrink it
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1    # remove left character from frequency map
                l += 1              # shrink window from the left
        
            result = max(result, r - l + 1)   # update result if window is valid
    
        return result