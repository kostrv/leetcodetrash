class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        # проверяем валидность индекса
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for i in range(index): # проходимся по связанным нодам в рамках индекса
            current = current.next
        
        return current.val


    def addAtHead(self, val: int) -> None:
        new_node = Node(val) # создаем новый узел

        new_node.next = self.head # внутри узла делаем ссылку на предыдущий 
        self.head = new_node # обновляем основную ссылку
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        new_node = Node(val) # создаем узел, в котором не будет ссылки

        if self.head is None: # если список пустой, новый узел становится головой
            self.head = new_node 
            self.size += 1
            return

        current = self.head 
        while current.next is not None: # доходим до крайнего начального значения 
            current = current.next
        
        # вставляем на его место новый узел
        current.next = new_node
        self.size += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: # больше длины — не вставляем
            return
        if index == 0:
            self.addAtHead(val) # вставка в начало — это addAtHead
            return
        if index == self.size: # вставка в конец — это addAtTail
            self.addAtTail(val)
            return

        new_node = Node(val)

        before = self.head # находим узел, который будет перед новым узлом
        for i in range(index-1):
            before = before.next
        
        # вставляем новый узел между before и before.next
        new_node.next = before.next 
        before.next = new_node
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or self.head is None: # проверяем валидность индекса и наличие элементов в списке
            return 
        if index == 0: # удаление первого элемента — просто обновляем ссылку на голову
            self.head = self.head.next
            self.size -= 1
            return
                
        before = self.head
        for i in range(index-1):
            before = before.next
        
        # удаляем узел, который находится после before
        before.next = before.next.next
        self.size -= 1


class Node: # класс для представления узла связного списка
    def __init__(self, val: int):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)