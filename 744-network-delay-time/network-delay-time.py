class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # создания списка смежности с пустым списком по умолчанию
        graph = {i: [] for i in range(1, n + 1)} 
        for source, target, travel_time in times:
            graph[source].append((target, travel_time))

        # по правилам релаксации, базовое значение расстояня - бесконечность
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0 # базовое время со старта

        # вершины, для которых уже найден конечный кратчайший путь
        visited = set()
        time = 0

        for _ in range(n):
            # находим непосещенную вершину вручную
            u = -1
            min_d = float('inf')
            
            for i in range(1, n + 1):
                if i not in visited and dist[i] < min_d:
                    min_d = dist[i]
                    u = i
                    
            #если вершина не была найдена (остались только бесконечности) выходим.
            if u == -1:
                break
                
            # помечаем вершину как обработанную
            visited.add(u)
            
            # релаксация всех соседей этой вершины
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight: # оптимизация соседей
                    dist[v] = dist[u] + weight

            
        max_delay = max(dist.values())
        
        # если до какого-то узла время осталось бесконечным, возвращаем -1
        return max_delay if max_delay != float('inf') else -1