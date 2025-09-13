class Solution(object):
    def maxFreqSum(self, s):
        con = 0
        vow = 0  
        d_set = set(s)  # to get unique characters
        for i in d_set:
            if i in "aeiou":
                vow = max(vow, s.count(i))  # count the vowel
            else:
                con = max(con, s.count(i))
        return con+vow  