class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        
        while True:
            # координаты апельсинов, которые будут отмечены в течении итерации
            to_mark = []
            
            # делаю похожим образом на алгоритм BF, перебирая все элементы
            for row in range(rows): 
                for c in range(cols):

                
                    if grid[row][c] == 2: # найден продвигающий элемент 
                        
                        # предполагаю координаты ближайших соседей элемента
                        p_neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                        for p_row, p_col in p_neighbours:
                            n_row, n_col = row + p_row, c + p_col # абсолютные координаты

                            # не выходим за границы и найден не отмеченный элемент
                            if 0 <= n_row < rows and 0 <= n_col < cols  and grid[n_row][n_col] == 1:

                                # добавляем в массив
                                if (n_row, n_col) not in to_mark:
                                    to_mark.append((n_row, n_col))
            
            # если нечего обрабатывать, выход
            if not to_mark:
                break
            
            # обработка элементов
            for r, c in to_mark:
                grid[r][c] = 2
            
            minutes += 1
            
        # финальная проверка
        for row in grid:
            if 1 in row:
                return -1
                
        return minutes