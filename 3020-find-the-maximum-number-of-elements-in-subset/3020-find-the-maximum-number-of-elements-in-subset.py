import sortedcontainers
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        sd = sortedcontainers.SortedDict()
        for num in nums:
            if num in sd:
                sd[num] = sd[num] + 1
            else:
                sd[num] = 1
        
        max_result = 0
        if 1 in sd:
            max_result = sd[1]-1 if sd[1]%2==0 else  sd[1]
            del sd[1]
        
        for key in sd:
            k = key
            res = 0
            while sd[k] >= 2 and k*k in sd:
                res += 2
                k = k*k
            res += 1
            max_result = max(max_result, res)
        return max_result
                