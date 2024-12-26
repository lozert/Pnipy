import numpy as np
from scipy.optimize import fsolve

# Определяем функцию
def equation(p):
    if p <= 0 or p >= 1/1.4:  # Проверка на допустимый диапазон p
        return np.inf  # Значения за пределами области определения
   
    return (
        -3*np.log2(p)
        - 3/ np.log(2)
    )

# Поиск корня численно
initial_guess = 0.1  # Начальное приближение
solution = fsolve(equation, initial_guess)

# Вывод результата
p = solution[0]

print(f"Решение: p = {p}")
