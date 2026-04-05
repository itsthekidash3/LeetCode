from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        freq = Counter(moves)
        return freq['R'] == freq["L"] and freq["U"] == freq["D"]
        


        
