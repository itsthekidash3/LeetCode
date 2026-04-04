# borrowed code from larry for better understanding
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        N = len(encodedText) # gives the total no of cells
        assert(N % rows == 0)
        cols = N// rows# gives the no of cols

        matrix = []

        for i in range(rows):
            matrix.append(encodedText[i*cols : (i+1)*cols])

        ans = []

        for i in range(cols):
            for j in range(rows):
                if j + i < cols:
                    ans.append(matrix[j][i+j])
        
        return "".join(ans).rstrip(" ")