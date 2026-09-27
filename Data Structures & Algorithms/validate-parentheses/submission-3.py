class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == ')':
                if stack and stack[-1] == '(':
                    del stack[-1]
                else:
                    return False
            elif char == ']':
                if stack and stack[-1] == '[':
                    del stack[-1]
                else:
                    return False
            elif char == '}':
                if stack and stack[-1] == '{':
                    del stack[-1]
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False