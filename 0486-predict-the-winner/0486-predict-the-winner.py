class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(i, j):
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            score = max(nums[j] - helper(i, j-1), nums[i] - helper(i+1, j))
            memo[(i, j)] = score
            
            return score
            
        memo = {}            
        return helper(0, len(nums)-1) >= 0