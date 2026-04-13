class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        # find the number and their index
        # hash map and store the value and the index :O(n)
        # then at the given value find the number closest to start: O(n)

        # find the position of the target
        indices = [i for i, x in enumerate(nums) if x == target]
        indices.sort()
        val = 99999
        for i in range(len(indices)):
            #minimum abs(i-start)
            val = min(val,abs(indices[i]-start))

        return val

        