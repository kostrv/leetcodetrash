class MyQueue:
    def __init__(self):
        # Используем два стека: один для хранения входящих элементов, другой для хранения элементов в порядке очереди
        self.stack = []
        self.queue = [] 

    def push(self, x: int) -> None:
        self.stack.append(x)

    def refill(self) -> None:
        # Функция для переноса элементов из стека в очередь, если очередь пуста. 
        if len(self.queue) == 0:
            while len(self.stack) != 0:
                self.queue.append(self.stack.pop())

    def pop(self) -> int:
        # Перед извлечением элемента из очереди, проверяем, нужно ли нам заполнить её элементами из стека.
        self.refill()
        return self.queue.pop()
        
    def peek(self) -> int:
        # Перед просмотром первого элемента очереди, проверяем, нужно ли нам заполнить её элементами из стека.
        self.refill()
        return self.queue[-1]

    def empty(self) -> bool:
        # Очередь считается пустой, если оба стека - и входящий, и очередь - пусты.
        return len(self.queue) == 0 and len(self.stack) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()