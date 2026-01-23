class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the word
        #sorted word as key, original word as value

        gAnagram = defaultdict(list) #list data structure

        for string in strs:
            sort = ''.join(sorted(string))
            gAnagram[sort].append(string)
        
        return list(gAnagram.values())
