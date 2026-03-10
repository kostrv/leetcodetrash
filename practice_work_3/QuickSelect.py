import random


def partition_by_lomuto(array: list, low: int, high: int) -> int:
    pivot = array[high]  # Выбираем опорный элемент (последний элемент массива)
    small_boundary = low - 1

    # Проходимся по всему массиву
    for i in range(low, high):
        if array[i] < pivot:  # Если элемент меньше опорного
            small_boundary += 1  # Двигаем границу
            array[small_boundary], array[i] = array[i], array[small_boundary]  # Меняем местами

    final_pivot = small_boundary + 1
    array[final_pivot], array[high] = array[high], array[final_pivot]  # Ставим pivot на финальное место

    return final_pivot


def quick_select(array: list, k: int, low: int = 0, high: int = None) -> int:
    high = high if high is not None else len(array) - 1

    # Случайно выбираем pivot и ставим его в конец, чтобы защититься от худшего случая
    random_pivot_index: int = random.randint(low, high)
    array[random_pivot_index], array[high] = array[high], array[random_pivot_index]

    # После партиции мы получаем pivot который стоит на позиции и разделяет массив на две части: меньшую и большую
    pivot_pos: int = partition_by_lomuto(array=array, low=low, high=high)

    if pivot_pos == k:
        return array[pivot_pos]  # pivot и есть k-й наименьший — готово

    elif pivot_pos > k:
        # k элемент левее pivot - используем левую часть рекурсией
        return quick_select(array=array, k=k, low=low, high=pivot_pos - 1)

    else:
        # k элемент правее pivot - используем правую часть рекурсией
        return quick_select(array=array, k=k, low=pivot_pos + 1, high=high)


if __name__ == '__main__':
    test_array = [3, 6, 8, 10, 1, 2, 1, 5, 4, 16, 17, 18, 19, 7, 9, 0, 11, 12, 13, 14, 15]
    print(f'Исходный массив: {test_array}')

    for k in [0, 1, 5, 10, 20]:
        result = quick_select(array=test_array[:], k=k)  # копия, чтобы не менять оригинал
        print(f'k={k} -> {result}')
        
