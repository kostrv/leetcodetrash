def partition_by_lomuto(array : list, low : int, high : int) -> int:
    pivot = array[high] # Выбираем опорный элемент (последний элемент массива)
    small_boundary = low - 1
    
    # Проходимся по всему массиву
    for i in range(low, high): 
        if array[i] < pivot: # Если элемент меньше опорного
            
            small_boundary += 1 # Двигаем границу
            array[small_boundary], array[i] = array[i], array[small_boundary] # Меняем местами 

    final_pivot = small_boundary + 1
    array[final_pivot], array[high] = array[high], array[final_pivot] # Меняем местами опорный элемент и элемент на границе

    return final_pivot


def quick_sort(array : list, low : int = 0, high : int = None) -> None:
    # Если границы не указаны, то устанавливаем их на начало и конец массива
    high = high if high is not None else len(array) - 1
    
    if low < high:
       pivot_pos = partition_by_lomuto(array=array, low=low, high=high)
       quick_sort(array=array, low=low, high=pivot_pos - 1) # Рекурсивно сортируем левую часть
       quick_sort(array=array, low=pivot_pos + 1, high=high) # Рекурсивно сортируем правую часть
    
    return array


if __name__ == '__main__':
    test_array = [3, 6, 8, 10, 1, 2, 1, 5, 4, 16, 17, 18, 19, 7, 9, 0, 11, 12, 13, 14, 15]
    print(f'Исходный массив: {test_array}')
    
    quick_sort(test_array)
    print(f'\n\nОтсортированный массив: {test_array}\n')