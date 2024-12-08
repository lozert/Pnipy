from mat_func import hooke_jeeves, nelder_mead, target_func, error_func
import numpy as np


 # Начальная догадка
x0 = [1, 1]

# Запуск метода Нелдера-Мида
result = nelder_mead(target_func, x0, error_func=None)

# Вывод результатов
print("\nРезультаты оптимизации:")
print(f"Оптимальная точка: {result['x']}")
print(f"Минимальное значение функции: {result['fun']}")
print(f"Количество итераций: {result['nit']}\n")

result = hooke_jeeves(target_func, x0, step_size=0.1, error_func=None)

print("Оптимальная точка:", result["x"])
print("Значение функции:", result["fun"])
print("Количество итераций:", result["nit"])