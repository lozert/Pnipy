import numpy as np

# Начальная симплекс-таблица с искусственными переменными (искусственная переменная a1, a2 и т.д.)
simplex_table = np.array([
    [0, -1, -3, 0, 0, 0, 0],  # Целевая функция: 3x1 + 2x2 + M(a1 + a2)
    [3, -1,  1, 1, 0, 0, 4],   # x1 + x2 - a1 = 4
    [20, 4,  3, 0, 1, 0, 2]    # x1 - x2 + a2 = 2
])

# Массив для индексов искусственных переменных
artificial_variables = [4, 5]  # Столбцы для искусственных переменных a1 и a2

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

# Первая фаза симплекс-метода: минимизация искусственных переменных
while np.any(simplex_table[0] < 0):  # Проверяем на отрицательные коэффициенты в целевой функции
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

# Проверяем наличие искусственных переменных в целевой функции после первой фазы
if np.any(simplex_table[0][artificial_variables] > 0):  # Если искусственные переменные не равны нулю
    print("Задача не имеет решения.")
else:
    print("Решение найдено, продолжаем со второй фазой...")

    # Вторая фаза симплекс-метода: продолжаем с обычной целевой функцией
    while np.any(simplex_table[0][:-1] < 0):
        pivot_col = np.argmin(simplex_table[0][:-1])
        pivot_row = find_pivot_row(simplex_table, pivot_col)
        
        simplex_table = update_simplex_table(simplex_table, pivot_row, pivot_col)

# Получаем значения переменных из симплекс-таблицы
x_values = simplex_table[1:, 0]  # Столбец значений переменных x1, x2, ...
f_value = simplex_table[0][0]    # Значение целевой функции

# Вывод результатов
print("\nРешение задачи:")
for i, x in enumerate(x_values, start=1):
    print(f"x{i} = {x:.2f}")
print(f"F(x) = {f_value:.2f}")
