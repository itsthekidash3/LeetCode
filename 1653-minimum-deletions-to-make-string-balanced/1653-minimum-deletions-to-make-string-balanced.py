class Solution:
    def minimumDeletions(self, s: str) -> int:
        # count the deletions
        # peek
        # if i< j & no b before a
        # pair of indices such  (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
        # greedy? or pointers? or sliding window? dp? stcak? Hashmap
        # using pointers is it O(n2)?
        # keep length
        #

        count = 0
        res = 0

        for ch in s:
            if ch == 'b':
                count += 1
            elif count:
                res += 1
                count -= 1
        
        return res