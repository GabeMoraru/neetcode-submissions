class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in ')}]' and len(arr) == 0:
                return False
            elif char in '({[':
                arr.append(char)
            elif char == ']' and arr[-1] == '[':
                arr.pop()
            elif char == '}' and arr[-1] == '{':
                arr.pop()
            elif char == ')' and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(char)                                     
        return len(arr) == 0