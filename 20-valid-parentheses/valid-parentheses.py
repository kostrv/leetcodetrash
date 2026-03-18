class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False 

                if pairs[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        
        return len(stack) == 0