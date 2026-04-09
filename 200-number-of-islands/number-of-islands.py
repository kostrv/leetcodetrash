class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def cleanup(row, col):
            # проверяем границы матрицы и воду
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            elif grid[row][col] == '0': 
                return

            # заменяем сушу на воду чтобы не считать по кругу
            grid[row][col] = '0'

            # запускаем лавину во все стороны
            cleanup(row + 1, col)
            cleanup(row - 1, col)
            cleanup(row, col + 1)
            cleanup(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                # нашли новый кусок земли
                if grid[r][c] == '1':
                    count += 1 
                    # убираем весь остров из поиска
                    cleanup(row=r, col=c)

        return count