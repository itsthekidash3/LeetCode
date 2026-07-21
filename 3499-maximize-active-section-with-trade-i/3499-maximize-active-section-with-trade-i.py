class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        ans=s.count('1')
        leftZeros=0
        delta=0
        i=0
        while i<n:
            rightZeros=0
            ones=0
            while i<n and s[i]=='1':
                ones+=1
                i+=1
            
            while i<n and s[i]=='0':
                rightZeros+=1
                i+=1
            if leftZeros and ones and rightZeros:
                delta=max(delta, leftZeros+rightZeros)
            
            leftZeros=rightZeros
        
        return ans+delta

            