class Solution:
    def maxArea(self, height: List[int]) -> int:
        # pointer = left and right
        #value at pointer and distance between them
        #if area is large, update the max area
        #if val at left is small, update left
        #if val at right is small update right

        max_area = 0
        left , right = 0, len(height)-1

        while left < right :

            max_area = max(max_area, (min(height[right], height[left]) * (right - left)))

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return max_area



        