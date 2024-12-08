import numpy as np
import matplotlib.pyplot as plt



def plot_frequency_distribution(frequencies):
    """
    Строит диаграмму попадания в диапазон от частоты попадания.
    
    :param frequencies: Список частот попадания
    :param bins: Диапазоны для построения гистограммы
    """
    bins = range(int(min(frequencies)) - 10, int(max(frequencies)) + 10, 5) 
    plt.figure(figsize=(10, 6))
    plt.hist(frequencies  , bins=bins, edgecolor='black', alpha=0.7)
    
    
    plt.title('Диаграмма попадения в диапазон от частоты попадания')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    x_ticks = np.arange(int(min(frequencies)), int(max(frequencies)) + 1, 20)  # Измените шаг на нужный
    plt.xticks(x_ticks)
    
    plt.grid(axis='y', alpha=0.75)
    
    plt.show(block=False)

def calculate_plot_m_d(massiv, h=50):
    m = []
    d = []
    
    # Определяем количество выстрелов (N)
    num_shots = len(massiv) // h
    
    # Итерируемся по количеству выстрелов
    for i in range(1, num_shots + 1):
        subset = massiv[:i * h]  # Берем подмассив
        m.append(np.mean(subset))  # Вычисляем среднее
        d.append(np.var(subset, ddof=1))  # Вычисляем выборочную дисперсию

    plt.figure(figsize=(12, 6))
    
    # График для M
    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(massiv) + 1, h), m, marker='o')
    plt.title('Зависимость M от количества выстрелов')
    plt.xlabel('Количество выстрелов (N)')
    plt.ylabel('Математическое ожидание (M)')
    
    # График для D
    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(massiv) + 1, h), d, marker='o', color='orange')
    plt.title('Зависимость D от количества выстрелов')
    plt.xlabel('Количество выстрелов (N)')
    plt.ylabel('Дисперсия (D)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Пример использования
    frequencies = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 8, 9, 10]
    bins = range(1, 12)  # Пример диапазонов

    plot_frequency_distribution(frequencies, bins)