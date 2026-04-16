# from heapq import heapify, heappop, heappush

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:

#         heap = [(0, 0)]   # стартуем с точки 0, вес входа = 0
#         heapify(heap)
#         visited = set()
#         total_cost = 0

#         while heap:
#             index, weight = heappop(heap)
#             x, y = points[index][0], points[index][1] 
            
#             for i in range(index+1, len(points)-1):
#                 if i in visited:
#                     continue 

#                 curr_x, curr_y = points[i][0], points[i][1] 
                
#                 visited.add(i)
#                 total_cost += (curr_x - x) + (curr_y - y)

#                 for j in range(i+1, len(points)-1):
#                     if j not in visited:
#                         heappush(heap, (j, (points[j][0] - curr_x) + (points[i][1] - curr_y)))
                
#         return total_cost




import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0
        
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            
            # Если точка уже в MST, пропускаем
            if i in visited:
                continue
            
            # Добавляем стоимость и помечаем точку
            total_cost += cost
            visited.add(i)
            
            # Добавляем в кучу расстояния от текущей точки до всех непосещенных
            curr_x, curr_y = points[i]
            for next_i in range(n):
                if next_i not in visited:
                    next_x, next_y = points[next_i]
                    # Манхэттенское расстояние с модулем!
                    dist = abs(curr_x - next_x) + abs(curr_y - next_y)
                    heapq.heappush(min_heap, (dist, next_i))
                    
        return total_cost