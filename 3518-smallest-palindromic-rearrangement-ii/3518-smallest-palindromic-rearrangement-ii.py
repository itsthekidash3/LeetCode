from collections import Counter 
from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count=Counter(s)
        halfway=[0]*26
        middle=""
        total=0
        for ch,f in count.items():
            index=ord(ch)- ord("a")
            halfway[index]=f//2
            total+=f//2
            if f%2:
                middle=ch
        def countWays():
            rem=total
            ways=1
            for y in halfway:
                if y:
                    ways *=comb(rem,y)
                    rem-=y
                    if ways>=k:
                        return k
            return ways
            
        if countWays() < k:
            return ""

        left=[]
      
        while total:
            for j in range(26):
                if halfway[j]==0:
                    continue
                halfway[j]-=1
                total-=1

                ways=countWays()

                if ways>=k:
                    left.append(chr(j+ord('a')))
                    break
                else:
                    k-=ways
                    halfway[j]+=1
                    total+=1
            
        left="".join(left)
        return left + middle + left[::-1]

        