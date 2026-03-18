class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        
        # операции для выполнения в зависимости от оператора
        self.operations = {
            '+' : lambda a, b: a + b,
            '-' : lambda a, b: a - b,
            '*' : lambda a, b: a * b,
            '/' : lambda a, b: int(a / b),
        }

        for el in tokens:
            # если элемент - оператор, выполняем соответствующую операцию над последними двумя элементами в стекe
            if el in ['+', '-', '*', '/']: 
                if len(self.stack) != 0:
                    first = self.stack.pop()
                    second = self.stack.pop()

                    # выполняем операцию и добавляем результат обратно в стек
                    new_val = self.operations[el](int(second), int(first))
                    self.stack.append(new_val)
            else:
               self.stack.append(el)

        # в конце в стеке останется единственный элемент - результат вычисления выражения, который мы возвращаем
        return int(self.stack[-1])