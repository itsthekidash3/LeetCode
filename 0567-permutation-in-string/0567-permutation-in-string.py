class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # Count character frequencies for s1 and the first window of s2 (size = len(s1))
        s1Count, s2Count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1
        
        # 'matches' tracks how many of the 26 characters have equal counts in both windows
        # If matches == 26, all characters match → current window is a permutation of s1
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0  # left pointer of the sliding window

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # --- Add new right character into the window ---
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1          # this character just became balanced
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1          # this character just became unbalanced (was balanced before +1)

            # --- Remove old left character from the window ---
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1          # this character just became balanced after removal
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1          # this character just became unbalanced (was balanced before -1)

            l += 1  # slide the window forward
        
        return matches == 26  # check the last window