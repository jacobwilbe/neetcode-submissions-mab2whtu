class Solution:

    def encode(self, strs: List[str]) -> str:
        result_str = ""
        for string in strs:
            result_str += str(len(string)) + "#" + string
        return result_str
    
    def decode(self, string: str) -> List[str]:
        result = []
        i = 0
        while i < len(string):
            j = i
            while string[j] != '#':
                j += 1
            length = int(string[i:j])
            i = j + 1
            j = i + length
            result.append(string[i:j])
            i = j
        return result


        

        



            

            

