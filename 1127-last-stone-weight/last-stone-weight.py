import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # эмулируем max-heap через инверсию знаков потмоу что, нам нужны два камня на каждом ходу
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            # извлекаем два самых тяжёлых
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            # если камни разного веса — возвращаем остаток обратно если равны — оба уничтожены, просто не добавляем ничего
            if x != y:
                heapq.heappush(heap, -(y - x))
        
        # если остался один камень — возвращаем его, иначе 0
        return -heap[0] if heap else 0