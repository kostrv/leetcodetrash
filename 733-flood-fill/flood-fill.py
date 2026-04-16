class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_row = sr
        start_col = sc

        start_color = image[start_row][start_col]

        # если цвет уже нужный то ничего делать не надо
        if start_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def search_in_width(row, col):
            # проверяем чтобы не вылететь за края картинки
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            # идем только если цвет совпадает с начальным
            elif image[row][col] != start_color:
                return

            # меняем старый цвет на новый
            image[row][col] = color

            # запускаем покраску для всех соседей рядом
            search_in_width(row + 1, col)
            search_in_width(row - 1, col)
            search_in_width(row, col + 1)
            search_in_width(row, col - 1)

        # начинаем заливку с точки старта
        search_in_width(start_row, start_col)
        return image