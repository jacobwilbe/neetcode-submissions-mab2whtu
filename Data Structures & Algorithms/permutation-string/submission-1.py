class Solution:
    def isPermutation(self, s1: str, s2: str)-> bool:
        a = sorted(s1)
        s1 = " ".join(a)
        b = sorted(s2)
        s2 = " ".join(b)

        for i in range(0, len(s1), 1):
            if s1[i] != s2[i]:
                return False 
        return True


    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1), len(s2) + 1):
            substring = s2[l:r]
            perm = self.isPermutation(substring, s1)
            if perm:
                return True
            l += 1
        return False

        