class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            length = str(len(item))
            res = res + length + "#" + item
        return res

         

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #length#string
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res


