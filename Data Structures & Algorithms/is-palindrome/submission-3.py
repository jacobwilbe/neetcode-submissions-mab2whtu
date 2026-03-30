class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat = "".join(filter(str.isalnum, s))
        concat = concat.lower()
        print(concat)
        i = 0
        j = len(concat) - 1
        while i < j:
            if concat[i] != concat[j]:
                return False
            i += 1
            j -= 1
        return True


        