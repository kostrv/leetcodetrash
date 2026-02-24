import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        for num in nums:
            heapq.heappush(self.heap, num)
            
            # выбрасываем минимум — он точно не входит в top-k так куча всегда хранит только k наибольших элементов
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # если новый элемент оказался меньше всех в куче, он сразу вылетит — min-heap сам вытолкнет его наверх и pop уберёт
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # корень min-heap — это минимум среди k наибольших, то есть ровно k-й наибольший элемент по всему потоку
        return self.heap[0]