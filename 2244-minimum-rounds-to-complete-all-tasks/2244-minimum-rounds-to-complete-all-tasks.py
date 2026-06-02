class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        count = 0
        for task, number in freq.items():
            if number == 1:
                return -1
            else :
                count += (number+2)//3
        
        return count