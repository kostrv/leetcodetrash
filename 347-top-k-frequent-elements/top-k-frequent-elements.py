import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # считаем частоту вхождений каждого элемента
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        
        for num, count in freq.items():
            # храним пары (частота, элемент) — куча сортирует по первому значению
            heapq.heappush(heap, (count, num))
            
            # выбрасываем наименее частый элемент — он точно не войдёт в top-k по частоте
            if len(heap) > k:
                heapq.heappop(heap)
        
        # извлекаем только сами элементы без их частот
        return [num for count, num in heap]