class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def refill(self) -> None:
        if len(self.queue) == 0:
            while len(self.stack) != 0:
                self.queue.append(self.stack.pop())

    def pop(self) -> int:
        self.refill()
        return self.queue.pop()
        
    def peek(self) -> int:
        self.refill()
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0 and len(self.stack) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()