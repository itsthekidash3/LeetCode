class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set1 = set(nums)
        count = 0
        

        for item in set1:
            if item - 1 not in set1:  #no start value
                length = 1
                while item + length in set1: #theres a next value in set
                    length += 1
                
                count = max(count, length)
        
        return count