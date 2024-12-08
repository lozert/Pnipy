import numpy as np
import matplotlib.pyplot as plt

# Пример матрицы данных (3 строки и 5 столбцов)
data = np.array([[1, 2, 3, 4, 5],
                 [2, 3, 4, 5, 6],
                 [3, 4, 5, 6, 7]])

# Вычисляем средние и максимальные значения по столбцам
mean_values = np.mean(data, axis=0)
max_values = np.max(data, axis=0)

# Создаем координаты для оси x
x = np.arange(len(mean_values))  # Индексы столбцов

# Устанавливаем ширину столбцов
width = 0.35

# Создаем график
plt.figure(figsize=(10, 6))

# Рисуем столбцы для средних значений
plt.bar(x, mean_values, width, label='Среднее', color='blue')

# Рисуем столбцы для максимальных значений, начиная с верхней части столбцов средних значений
plt.bar(x, max_values, width, label='Максимальное', bottom=mean_values, color='orange')

# Добавляем заголовок и метки осей
plt.title('Накладывающиеся средние и максимальные значения по столбцам')
plt.xlabel('Индекс столбца')
plt.ylabel('Значение')

# Добавляем легенду и сетку
plt.legend()
plt.grid()

# Устанавливаем метки по оси x
plt.xticks(x, [f'Столбец {i}' for i in range(len(mean_values))])

# Показываем график
plt.tight_layout()
plt.show()
