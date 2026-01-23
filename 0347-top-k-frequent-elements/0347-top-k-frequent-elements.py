from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #most repeated element. that is in top k 
        #frequency as key with num as value

        # worst case : every single value is distinct
        # heapify o(log n)
        # o(n)
        # bucket size is input array size
        # scan from last coz, most frequent element

        bucket = [[] for _ in range(len(nums)+1)] 

        count = Counter(nums)
        for num, freq in count.items():
            bucket[freq].append(num)
        res = []

        for i in range(len(nums),0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


                    #the psuedocode is where lose !. I need to understand that better !!


















        