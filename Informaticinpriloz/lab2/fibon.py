def fibonacci(n):
    """
    Возвращает список из первых n чисел Фибоначчи.
    
    Параметры:
    n (int): Количество чисел Фибоначчи для генерации.
    
    Возвращает:
    list: Список из n чисел Фибоначчи.
    
    Исключения:
    ValueError: Если n <= 0 или не является целым числом.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть положительным целым числом.")
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n]


import pytest


def test_fibonacci_positive():
    """
    Тест для корректных входных данных.
    Проверяем корректность результата для положительных значений n.
    """
    assert fibonacci(1) == [0], "Должен возвращаться список [0] для n = 1"
    assert fibonacci(2) == [0, 1], "Должен возвращаться список [0, 1] для n = 2"
    assert fibonacci(5) == [0, 1, 1, 2, 3], "Должен возвращаться список [0, 1, 1, 2, 3] для n = 5"

def test_fibonacci_invalid_inputs():
    """
    Тест для некорректных входных данных.
    Проверяем, что выбрасываются исключения для некорректных значений n.
    """
    with pytest.raises(ValueError, match="n должно быть положительным целым числом."):
        fibonacci(0)
    with pytest.raises(ValueError, match="n должно быть положительным целым числом."):
        fibonacci(-1)
    with pytest.raises(ValueError, match="n должно быть положительным целым числом."):
        fibonacci(3.5)

def test_fibonacci_boundary_values():
    """
    Тест для граничных значений.
    Проверяем результат для минимальных граничных значений n.
    """
    assert fibonacci(1) == [0], "Граничное значение n = 1 должно возвращать [0]"
    assert fibonacci(2) == [0, 1], "Граничное значение n = 2 должно возвращать [0, 1]"

test_fibonacci_positive()
test_fibonacci_invalid_inputs()
test_fibonacci_boundary_values()