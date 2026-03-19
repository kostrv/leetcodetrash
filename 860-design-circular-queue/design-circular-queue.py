class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0 # указатель на начало очереди
        self.tail = 0 # указатель на конец очереди
        self.size = 0 # текущий размер очереди
        self.capacity = k # максимальная емкость очереди
                
        # инициализируем очередь фиксированного размера
        self.queue = [0] * self.capacity 
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # добавляем элемент в позицию, на которую указывает tail, и затем перемещаем tail вперед по кругу        
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # удаляем элемент в позиции, на которую указывает head, и затем перемещаем head вперед по кругу
        self.queue[self.head] = 0
        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        # возвращаем элемент в позиции, на которую указывает head, который является передним элементом очереди
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        # возвращаем элемент в позиции, на которую указывает tail - 1, который является задним элементом очереди
        return self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self) -> bool:
        # очередь считается пустой, если размер равен нулю.
        return self.size == 0

    def isFull(self) -> bool:
        # очередь считается полной, если размер равен максимальной емкости.
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()