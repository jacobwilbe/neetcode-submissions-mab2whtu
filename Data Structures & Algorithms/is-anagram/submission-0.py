class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ordS = sorted(s)
        ordT = sorted(t)
        for i in range(len(s)):
            if ordS[i] != ordT[i]:
                return False
        return True
        