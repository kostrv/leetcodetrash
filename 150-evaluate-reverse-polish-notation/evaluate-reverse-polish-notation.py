class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        self.operations = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b),
        }

        for el in tokens:
            if el in ["+", "-", "*", "/"]:
                if len(self.stack) != 0:
                    first = self.stack.pop()
                    second = self.stack.pop()

                    new_val = self.operations[el](int(second), int(first))
                    self.stack.append(new_val)
            else:
               self.stack.append(el)
    
        return int(self.stack[-1])