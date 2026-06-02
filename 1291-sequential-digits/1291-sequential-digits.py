class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        arr = []
        for i in range(9):
            for j in range(i,9):
                num = s[i:j+1]
                if low <= int(num) <= high:
                    arr.append(int(num))
        arr.sort()
        return arr

        