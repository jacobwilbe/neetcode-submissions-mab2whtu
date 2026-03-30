class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        noDupes = sorted(set(nums))
        noDupes = list(noDupes)
        print(noDupes)
        if len(noDupes) == 1:
            return 1
        sequence = 1
        maxSequence = 0 
        flag = False
        for i in range(1, len(noDupes)):
            if noDupes[i] == (1 + noDupes[i-1]):
                flag = True
            if noDupes[i] != (1 + noDupes[i-1]):
                flag = False
                if sequence > maxSequence:
                    maxSequence = sequence
                sequence = 1
            if flag:
                sequence += 1
                if i == (len(noDupes) - 1) and (maxSequence == 0 or sequence > maxSequence):
                    maxSequence = sequence
        return maxSequence



        