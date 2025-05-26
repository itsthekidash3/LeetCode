from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       bucket = [[] for _ in range(len(nums)+1)]  #creating a bucket
       count = Counter(nums) #count ={} for n in nums:count[n] = 1+count.get(1,0)
       for num, freq in count.items():
        bucket[freq].append(num) #adding values to bucket by taking key and value pair
       res = []
       
       for i in range(len(nums), 0 , -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res 

        