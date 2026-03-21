class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection (Tortoise and Hare)
        # Key insight: treat array as implicit linked list where nums[i] points to index nums[i]
        # The duplicate creates a cycle (multiple indices point to same value)
        
        # Mathematical proof:
        # Let p = distance from start to cycle entrance
        # Let c = cycle length
        # Let x = distance from cycle entrance to first intersection point
        # 
        # When slow and fast meet:
        # - Slow has traveled: p + c - x (reached cycle entrance, went around, backed up x)
        # - Fast has traveled: p + 2c - x (same path but went around cycle twice)
        # - Fast travels 2x the distance of slow: 2(p + c - x) = p + 2c - x
        # 
        # Solving: 2p + 2c - 2x = p + 2c - x
        #          2p - 2x = p - x
        #          p = x
        # 
        # This proves: distance from start to cycle entrance = 
        #              distance from intersection to cycle entrance
        
        # Phase 1: Find intersection point inside the cycle
        # Slow moves 1 step, fast moves 2 steps
        # They will meet inside the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (the duplicate)
        # Since p = x, moving from both start and intersection will meet at entrance
        # Move both pointers 1 step at a time until they meet
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow  # This is the duplicate value