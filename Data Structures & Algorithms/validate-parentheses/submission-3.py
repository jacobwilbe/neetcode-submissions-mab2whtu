class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"}": "{", ")" : "(", "]" : "["}

        stack = []
        for p in s:
            if p in closing:
                if not stack:
                    return False
                if stack[-1] != closing[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return not stack

            
                