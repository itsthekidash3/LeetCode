class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 #edge case

        l, r = 0, len(height) - 1

        leftMax, rightMax =  height[l], height[r]

        res = 0

        while l < r:

            if leftMax < rightMax:
                l += 1 #move left pointer
                leftMax = max(leftMax, height[l])  #updating the leftmax
                res += leftMax - height[l]

            else:
                r -= 1 #move right pointer
                rightMax = max(rightMax, height[r]) #updating the right max
                res += rightMax - height[r]
        
        return res