class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0


        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def cleanup(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols: # выход за границы
                return
            elif grid[row][col] == '0': 
                return

            grid[row][col] = '0'

            cleanup(row + 1, col)
            cleanup(row - 1, col)
            cleanup(row, col + 1)
            cleanup(row, col - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1 
                    cleanup(row=r, col=c)

        return count