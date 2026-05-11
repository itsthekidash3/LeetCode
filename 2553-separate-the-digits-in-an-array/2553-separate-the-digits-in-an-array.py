class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def rev(num):
            curr=[]
            while num:
                last=num%10
                curr.append(last)
                num//=10
            curr=curr[::-1]
            nonlocal res
            res.extend(curr)
        res=[]
        for num in nums:
            rev(num)
        return res