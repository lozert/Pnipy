import numpy as np

M = 1e6

# Инициализация симплекс-таблицы
simplex_table = np.array([
    [-M, -M-7, -M+2, 0, M, 0, 0, 0],  # Целевая функция с большим M
    [3, 5, -2, 1, 0, 0, 0, 0],         # Ограничения и искусственные переменные
    [1, 1, 1, 0, -1, 0, 0, 1],
    [3, -3, 1, 0, 0, 1, 0, 0],
    [4, 2, 1, 0, 0, 0, 1, 0]
])


def find_pivot_row(matrix, pivot_col):
    """
    Находит индекс строки для разрешающего элемента (разрешающая строка).
    Учитывает только неотрицательные значения.
    """
    ratios = []
    for i in range(1, len(matrix)):
        # Вычисляем отношение значения к элементу разрешающего столбца
        element = matrix[i][pivot_col]
        if element > 0:  # Учитываем только положительные элементы столбца
            ratios.append(matrix[i][0] / element)
        else:
            ratios.append(float('inf'))  # Исключаем отрицательные элементы
    return np.argmin(ratios) + 1  # +1, так как первая строка — целевая функция

def update_simplex_table(matrix, pivot_row, pivot_col):
    """
    Обновляет симплекс-таблицу на основе разрешающего элемента.
    """
    new_matrix = np.zeros_like(matrix, dtype=float)
    
    # Обновляем разрешающую строку
    new_matrix[pivot_row] = matrix[pivot_row] / matrix[pivot_row][pivot_col]
    
    # Обновляем остальные строки
    for i in range(len(matrix)):
        if i == pivot_row:
            continue
        for j in range(len(matrix[0])):
            new_matrix[i][j] = matrix[i][j] - (
                matrix[i][pivot_col] * matrix[pivot_row][j]
            ) / matrix[pivot_row][pivot_col]
    
    return new_matrix

# Список для хранения базисных переменных
basis_elements = []

# Цикл, пока есть отрицательные значения в первой строке
while np.any(simplex_table[0] < 0):
    # Находим индекс разрешающего столбца
    pivot_col = np.argmin(simplex_table[0])
    
    # Находим индекс разрешающей строки
    try:
        pivot_row = find_pivot_row(simplex_table, pivot_col)
    except ValueError:
        print("Нет допустимых решений (неограниченная задача).")
        break
    
    # Сохраняем индексы базисных переменных
    basis_elements.append((pivot_row, pivot_col))
    
    # Обновляем симплекс-таблицу
    simplex_table = update_simplex_table(simplex_table, pivot_row, pivot_col)
    print(f"Обновлённая симплекс-таблица:\n{simplex_table}\n")

# Вывод результатов
print("Результаты:")
for row, col in basis_elements:
    print(f"x{col} = {simplex_table[row][0]}")
print(f"F(x) = {simplex_table[0][0]}")
