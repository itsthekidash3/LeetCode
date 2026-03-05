class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search on a rotated sorted array
        # Key insight: At any midpoint, at least one half (left or right) is guaranteed to be sorted
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Found the target
            if target == nums[mid]:
                return mid
            
            # Determine which half is sorted by comparing left boundary with mid
            
            # Left half is sorted (nums[l] to nums[mid] is in ascending order)
            if nums[l] <= nums[mid]:
                # Check if target is within the sorted left half's range
                if target > nums[mid] or target < nums[l]:
                    # Target is NOT in sorted left half, must be in right half
                    l = mid + 1
                else:
                    # Target IS in sorted left half (nums[l] <= target < nums[mid])
                    r = mid - 1
            
            # Right half is sorted (nums[mid] to nums[r] is in ascending order)
            else:
                # Check if target is within the sorted right half's range
                if target < nums[mid] or target > nums[r]:
                    # Target is NOT in sorted right half, must be in left half
                    r = mid - 1
                else:
                    # Target IS in sorted right half (nums[mid] < target <= nums[r])
                    l = mid + 1
        
        # Target not found in array
        return -1