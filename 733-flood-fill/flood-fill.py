class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_row = sr
        start_col = sc

        start_color = image[start_row][start_col]

        if start_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def search_in_width(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols: # выход за границы
                return
            elif image[row][col] != start_color: # не идем к тем узлам, который не соответствуют по цвету
                return

            image[row][col] = color

            # поиск по соседям
            search_in_width(row + 1, col)
            search_in_width(row - 1, col)
            search_in_width(row, col + 1)
            search_in_width(row, col - 1)

        search_in_width(start_row, start_col)
        return image