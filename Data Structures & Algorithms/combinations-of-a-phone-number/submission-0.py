class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        chars = []
        d_c = {}
        for j in range(2,10):
            k = str(j)
            d_c[k] = letters[j-2]
        def dfs(i):
            if i >= len(digits):
                if chars:
                    res.append("".join(chars))
                return

            for c in d_c[digits[i]]:
                chars.append(c)
                dfs(i+1)
                chars.pop()
        dfs(0)
        return res

