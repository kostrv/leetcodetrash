import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = x**2 + y**2
            
            # храним max-heap через негативное расстояние, heapq всегда min, поэтому инвертируем знак
            heapq.heappush(heap, (-dist, x, y))
            
            # выбрасываем самую дальную точку если размер превысил k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # возвращаем только координаты
        return [[x, y] for _, x, y in heap]