class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create mapping to empty list
        result = []
        mapping = defaultdict(list)
        #sorted anagram will be a key 
        #hash anagrams to their sorted key  

        for string in strs:
            key = "".join(sorted(string))
            mapping[key].append(string)
        for k,v in mapping.items():
            result.append([string for string in v])
        
        return result

        




