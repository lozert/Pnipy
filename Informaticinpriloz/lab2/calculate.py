def calculator(num1, num2, operation):
    """
    Выполняет арифметическую операцию между двумя числами.
    
    Параметры:
    num1 (int/float): Первое число.
    num2 (int/float): Второе число.
    operation (str): Операция (+, -, *, /).
    
    Возвращает:
    float: Результат арифметической операции.
    
    Исключения:
    ValueError: Если операция не поддерживается или происходит деление на ноль.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Оба аргумента должны быть числами.")
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно.")
        return num1 / num2
    else:
        raise ValueError("Неподдерживаемая операция. Используйте +, -, *, /.")

import pytest


def test_calculator_addition():
    """
    Тест для операции сложения.
    Проверяем правильность выполнения сложения.
    """
    assert calculator(3, 5, '+') == 8, "Сложение 3 + 5 должно быть 8"
    assert calculator(1.2, 3.4, '+') == 4.6, "Сложение 1.2 + 3.4 должно быть 4.6"

def test_calculator_subtraction():
    """
    Тест для операции вычитания.
    Проверяем правильность выполнения вычитания.
    """
    assert calculator(5, 3, '-') == 2, "Вычитание 5 - 3 должно быть 2"
    assert calculator(3.5, 1.2, '-') == 2.3, "Вычитание 3.5 - 1.2 должно быть 2.3"

def test_calculator_multiplication():
    """
    Тест для операции умножения.
    Проверяем правильность выполнения умножения.
    """
    assert calculator(4, 2, '*') == 8, "Умножение 4 * 2 должно быть 8"
    assert calculator(1.5, 3, '*') == 4.5, "Умножение 1.5 * 3 должно быть 4.5"

def test_calculator_division():
    """
    Тест для операции деления.
    Проверяем правильность выполнения деления.
    """
    assert calculator(8, 2, '/') == 4, "Деление 8 / 2 должно быть 4"
    assert calculator(9, 3, '/') == 3, "Деление 9 / 3 должно быть 3"

def test_calculator_zero_division():
    """
    Тест для деления на ноль.
    Ожидаемое поведение: выброс исключения ValueError.
    """
    with pytest.raises(ValueError, match="Деление на ноль невозможно."):
        calculator(5, 0, '/')

def test_calculator_invalid_operation():
    """
    Тест для некорректной операции.
    Проверяем выброс исключения ValueError для неправильных операций.
    """
    with pytest.raises(ValueError, match="Неподдерживаемая операция. Используйте \\+, \\-, \\*, \\/."):
        calculator(3, 5, 'x')

def test_calculator_invalid_arguments():
    """
    Тест для некорректных аргументов.
    Проверяем выброс исключения ValueError для нечисловых аргументов.
    """
    with pytest.raises(ValueError, match="Оба аргумента должны быть числами."):
        calculator("abc", 5, '+')
    with pytest.raises(ValueError, match="Оба аргумента должны быть числами."):
        calculator(4, "xyz", '-')
