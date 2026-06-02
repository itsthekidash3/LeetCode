class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def solve(start1, duration1, start2, duration2):
            finish1 = float('inf')

            # find finish1
            for s, d in zip(start1, duration1):
                finish1 = min(finish1, s + d)

            finish2 = float('inf')

            # find finish2
            for s, d in zip(start2, duration2):
                new_s = max(s, finish1)
                finish2 = min(finish2, new_s + d)

            return finish2

        # land -> water
        land2water = solve(landStartTime, landDuration, waterStartTime, waterDuration)

        # water -> land 
        water2land = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land2water, water2land)