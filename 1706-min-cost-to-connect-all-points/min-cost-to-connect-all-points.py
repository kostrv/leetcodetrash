
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)]  # (стоимость пути, индекс)
        total_cost = 0
        
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            
            # если точка уже обработана, пропускаем
            if i in visited:
                continue
            
            # добавляем стоимость и помечаем точку
            total_cost += cost
            visited.add(i)
            
            curr_x, curr_y = points[i]
            
            # Добавляем в кучу расстояния от текущей точки до всех непосещенных
            for next_i in range(n):
                if next_i not in visited:
                    next_x, next_y = points[next_i]
                    
                    # рассчитываем разницу с текущей точкой, нужно использовать модуль, чтобы избежать отрицательного расстояния
                    dist = abs(curr_x - next_x) + abs(curr_y - next_y)

                    # добавляем в конец точку
                    heapq.heappush(heap, (dist, next_i))
                    
        return total_cost