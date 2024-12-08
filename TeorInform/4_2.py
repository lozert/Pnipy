import numpy as np
import matplotlib.pyplot as plt

# Данные
M = 3  # мощность алфавита
k = 3  # длина исходной последовательности
n = 5  # длина кодовой последовательности
P_e = 0.1  # вероятность ошибки

# Логарифм от M в двоичной системе
log_M = np.log2(M)

# Скорость кода без учета ошибки
R = (k * log_M) / n

# Энтропия ошибки H(P_e)
H_Pe = -P_e * np.log2(P_e) - (1 - P_e) * np.log2(1 - P_e)

# Скорость с учетом ошибки
R_corrected = R - H_Pe

# Вывод значений
R, H_Pe, R_corrected

print(R, H_Pe, R_corrected)

# Рассмотрим разные значения k (длина исходной последовательности)
k_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Рассчитаем скорость R для каждого k
R_values = (k_values * log_M) / n

# Формирование таблицы значений
print(list(zip(k_values, R_values)))
