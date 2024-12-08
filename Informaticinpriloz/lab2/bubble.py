def bubble_sort(arr):
    """
    Выполняет сортировку списка чисел методом пузырька.
    
    Параметры:
    arr (list): Список чисел для сортировки.
    
    Возвращает:
    list: Отсортированная копия списка.
    
    Исключения:
    ValueError: Если входные данные не являются списком чисел или пустым списком.
    """
    if not isinstance(arr, list):
        raise ValueError("Ожидается список.")
    
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Все элементы списка должны быть числами.")
    
    n = len(arr)
    sorted_arr = arr.copy()
    
    # Алгоритм пузырьковой сортировки
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    
    return sorted_arr


import pytest


def test_bubble_sort_valid_input():
    """
    Тест для валидных данных.
    Проверяем корректность сортировки для различных случаев.
    """
    assert bubble_sort([3, 1, 2]) == [1, 2, 3], "Сортировка списка [3, 1, 2] должна вернуть [1, 2, 3]"
    assert bubble_sort([-1, 0, 5.5]) == [-1, 0, 5.5], "Сортировка списка [-1, 0, 5.5] должна вернуть [-1, 0, 5.5]"
    assert bubble_sort([1]) == [1], "Сортировка списка с одним элементом [1] должна вернуть [1]"
    assert bubble_sort([2, 1]) == [1, 2], "Сортировка списка [2, 1] должна вернуть [1, 2]"

def test_bubble_sort_empty_list():
    """
    Тест для пустого списка.
    Ожидаемое поведение: пустой список остается пустым.
    """
    assert bubble_sort([]) == [], "Пустой список должен остаться пустым."

def test_bubble_sort_invalid_type():
    """
    Тест для некорректных типов входных данных.
    Проверяем выброс исключения для не списка и не числовых элементов.
    """
    with pytest.raises(ValueError, match="Ожидается список."):
        bubble_sort("abc")  # Строка вместо списка
    with pytest.raises(ValueError, match="Ожидается список."):
        bubble_sort(123)  # Число вместо списка

def test_bubble_sort_non_numeric_elements():
    """
    Тест для списка с нечисловыми элементами.
    Проверяем выброс исключения для списка с нечисловыми значениями.
    """
    with pytest.raises(ValueError, match="Все элементы списка должны быть числами."):
        bubble_sort([1, 2, "a"])  # Наличие строки в списке
    with pytest.raises(ValueError, match="Все элементы списка должны быть числами."):
        bubble_sort([3, None, 4])  # Наличие None в списке
