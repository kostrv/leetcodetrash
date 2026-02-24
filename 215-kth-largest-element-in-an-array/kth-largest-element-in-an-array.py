import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > k: # Используем данное условие для того, чтобы получить k в корне кучи
                heapq.heappop(heap)
        
        return heap[0]