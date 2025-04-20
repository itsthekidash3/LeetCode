class Solution(object):
    def numRabbits(self, answers):
        mpp = Counter(answers)
        total = 0
        for x in mpp:
            total += ceil(float(mpp[x]) / (x + 1)) * (x + 1) # no of groups, present in each group
        return int(total)
