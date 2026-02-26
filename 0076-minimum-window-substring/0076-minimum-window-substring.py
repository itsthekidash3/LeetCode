class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""

        countT, window = {}, {}

        # Build frequency map for t — this is our "target" we need to satisfy
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0           # how many unique chars currently meet their required frequency
        need = len(countT) # how many unique chars we need to satisfy (not total chars, unique ones)

        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)  # expand window to the right

            # Check if this new character just fulfilled a requirement.
            # We only care once window[c] exactly hits countT[c] — going over doesn't count again
            if c in countT and window[c] == countT[c]:  
                have += 1

            # Once we have a valid window, try shrinking from the left to minimize it
            while have == need:
                # Update result if this window is smaller than the best we've seen
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # Remove the leftmost character and shrink the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:  
                    have -= 1  # we no longer satisfy this character's requirement

                l += 1  # move left pointer forward

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""  