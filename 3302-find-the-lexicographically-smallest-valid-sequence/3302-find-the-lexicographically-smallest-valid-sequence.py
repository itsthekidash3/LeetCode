class Solution:
    def validSequence(self, s1: str, s2: str) -> List[int]:
        n=len(s1)
        m=len(s2)
        # For Storing the last_index of each char in S2
        last_index=[0]*m
        j=m-1
        i=n-1
        # Finding the last_index of each char in S2
        while i>=0 and j>=0:
            if s1[i]==s2[j]:
                last_index[j]=i
                j-=1
            i-=1
        # For tracking that One Different Letter
        Took=0
        index=[]
        j=0
        for i in range(n):
            # Reached the End of S2 so True
            if j==m:
                break
            # If they are same then pick the index
            if s1[i]==s2[j]:
                index.append(i)
                j+=1
            else:
                # If not Equal and have Changed a char already then 
                # continue as you may have chance of finding the others
                # on S1[i+1:]
                if Took:
                    continue
                # If not taken and you are at the end of S2 
                # then its possible as you can change S2[m-1]
                if j==m-1:
                    index.append(i)
                    break
                # If not reached the end and
                # next char of S2 can be reached then pick this index
                if last_index[j+1]>i:
                    index.append(i)
                    # Mark it as taken
                    Took=1
                    j+=1
        return index if len(index)==m else []