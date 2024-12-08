import numpy as np
import time 
from utils.interval_filter import count_num_range, count_num_interval
import os

RAND_MAX = np.uint64(2**64 - 1)

def rand(size, next_val=np.uint64(11)):
    a = np.uint64(6364136223846793005)
    c = np.uint64(1442695040888963407)
    m = np.uint64(2**64 - 1)
    
    # Создаем массив индексов для всех значений от 0 до size-1
    indices = np.arange(size, dtype=np.uint64)

    # Векторизованная операция для генерации всех значений за один раз
    # next_vals[i] = (next_val * a^i + c * i) % m
    a_powers = np.power(a, indices, dtype=np.uint64)  # Возводим 'a' в степени индексов
    next_vals = (next_val * a_powers + c * indices) % m  # Применяем генерацию для всех значени й
    
    # Преобразуем к необходимому диапазону для RAND_MAX
    result = (next_vals / (RAND_MAX - 1)).astype(np.float64)
    return result




start = time.time()
# Пример использования
massive_size = 1_000_000  # Генерация миллиона случайных чисел
massive = rand(massive_size)
end = time.time()

print(f"Время выполнения {(end-start):.4f} сек")



unique_values, indices = np.unique(massive, return_index=True)

# Сортируем индексы и получаем уникальный массив
unique_array = unique_values[np.argsort(indices)]

try:
    min_size = min(massive.size, unique_array.size)

    a_truncated = massive[:min_size]
    b_truncated = unique_array[:min_size]

    indices = np.where(a_truncated != b_truncated)[0]

    # Вывод индексов
    print(f'Элементы перестали совпадать на индексах: {indices[0]}')
    print(f"Элементы {a_truncated[indices[0]]} и {b_truncated[indices[0]]}")
except:
    print("Нет повторяющихся элементов")

print(len(massive))  # Количество сгенерированных чисел
print(len(unique_array))  # Количество уникальных значений


expected_value = np.mean(massive) # мат ожидание 
variance = np.var(massive, ddof=1) # дисперсия
sqrt_var = np.sqrt(variance) # среднеквадратичное 
count_range = count_num_range(massive, 0.5, sqrt_var) / massive_size * 100
count_interval = count_num_interval(massive, 0, 0.5)

print(f"Минимальное значение {massive.min():.6f} , Максимальное значение {massive.max():.6f}")
print(f"Математическое ожидание: {expected_value:.5f}")
print(f"Дисперсия: {variance:.5f}")
print(f"Среднеквадратичное отклонение: {sqrt_var:.5f}")
print(f"Частотный тест: {count_range:.3f}%")
print(f"Количество чисел в интервале [0, 0.5] = {count_interval} и [0.5, 1] = {massive_size - count_interval}")