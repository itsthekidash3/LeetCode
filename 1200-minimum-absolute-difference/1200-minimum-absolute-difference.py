class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini = float('inf')
        res = []

        for i in range(len(arr)-1):
            
            diff = arr[i+1] - arr[i] 
            if diff < mini :
                mini = diff
                res = [[arr[i], arr[i+1]]]

            elif diff == mini :
                res.append([arr[i],arr[i+1]])
        return res
        