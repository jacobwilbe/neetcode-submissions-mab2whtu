class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramSet = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in anagramSet:
                anagramSet[key].append(word)
            else:
                anagramSet[key] = [word]
        return [val for val in anagramSet.values()]
