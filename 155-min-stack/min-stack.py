class MinStack:

    def __init__(self):
        self.stack = [] # основной стек для хранения всех значений
        self.minStack = [] # стек для хранения минимальных значений

    def push(self, val: int) -> None:
        self.stack.append(val) # добавляем элемент в основной стек
        
        # если новый элемент меньше или равен текущему минимуму, добавляем его в стек минимумов
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val) 
    
    def pop(self) -> None: 
        # удаляем верхний элемент из основного стека
        top = self.stack[-1]
        self.stack.pop()
        
        # если удаленный элемент был текущим минимумом, удаляем его из стека минимумов
        if top == self.minStack[-1]:
            self.minStack.pop()

    # возвращаем верхний элемент основного стека
    def top(self) -> int: 
        return self.stack[-1]

    # возвращаем верхний элемент стека минимумов, который является текущим минимумом
    def getMin(self) -> int: 
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()