import numpy as np

# Изначальный список
m = [1, 3, 4, 5]

# Преобразование списка в массив NumPy
m_array = np.array(m)

# Поэлементное сравнение
in_interval = np.sum((m_array >= 0) & (m_array <= 10))



print(in_interval)
