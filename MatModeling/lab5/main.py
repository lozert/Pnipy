import numpy as np
from utils.draw_graph import plot_frequency_distribution, calculate_plot_m_d
# Заданные значения
L_target = 1000  # Дальность выстрела, м
g = 9.81  # Ускорение свободного падения, м/с^2
alpha = np.radians(30)  # Угол выстрела в радианах


V_0 = np.sqrt(L_target * g / np.sin(2 * alpha))


mv = 50  # Математическое ожидание для скорости
sigma_v = 3  # Среднеквадратическое отклонение для скорости
m_alpha = alpha  # Математическое ожидание для угла
sigma_alpha = np.radians(5)  # Среднеквадратическое отклонение для угла, переводим в радианы


N = 30000  # Количество выстрелов (итераций)
Delta = 3  # Размер мишени (в метрах)

# Генерация случайных значений для скорости и угла по нормальному распределению
V_samples = np.random.normal(mv, sigma_v, N)
alpha_samples = np.random.normal(m_alpha, sigma_alpha, N)

# Расчёт дальности для каждого набора значений V и alpha
X_samples = (V_samples ** 2 * np.sin(2 * alpha_samples)) / g

plot_frequency_distribution(X_samples)
calculate_plot_m_d(X_samples)


# Вероятность попадания в цель размером Delta
hits = np.sum((X_samples >= (L_target - Delta / 2)) & (X_samples <= (L_target + Delta / 2)))
hit_probability = hits / N

# Математическое ожидание и дисперсия дальности
M = np.mean(X_samples)
D = np.var(X_samples)

# Определение границ для 3 сигм
lower_bound = M - 3 * np.sqrt(D)
upper_bound = M + 3 * np.sqrt(D)


# Подсчет количества попаданий в диапазон
hits_within_bounds = np.sum((X_samples >= lower_bound) & (X_samples <= upper_bound))
totaX_samples = len(X_samples)

# Вычисление процента попадений
hit_percentage = (hits_within_bounds / N) * 100
# Вывод результатов
print(f"Начальная скорость V_0 для дальности {L_target} м: {mv:.2f} м/с")
print(f"Средняя дальность: {M:.2f} м")
print(f"Вероятность попадания в цель: {hit_probability * 100:.2f}%")
print(f"Математическое ожидание дальности: {M:.2f} м")
print(f"Дисперсия дальности: {D:.2f} м^2")
print(f"Процент попадения в диапазон 3 сигм: {hit_percentage:.5f}%")
