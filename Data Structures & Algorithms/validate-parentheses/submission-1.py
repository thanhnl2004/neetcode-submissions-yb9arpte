class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = { ')': '(', ']': '[', '}': '{'}
        for c in s:
            if not stack or c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and stack[-1] != '(' or c == ']' and stack[-1] != '[' or c == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
                

        return not stack



                
            
        