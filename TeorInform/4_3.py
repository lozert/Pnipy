import numpy as np
import matplotlib.pyplot as plt

# Настройки
p_values = [0.02, 0.01, 0.03]
e = 0.01
n_max = 10
num_experiments = 10000

# Функция для проведения эксперимента
def simulate_errors(p, e, n_max, num_experiments):
    error_probabilities = []
    
    for n in range(1, n_max + 1):
        total_errors = 0
        total_symbols = 0
        
        for _ in range(num_experiments):
            # Генерация блока данных
            block = np.random.choice([0, 1], size=n, p=[1-p, p])
            
            # Ввод случайной ошибки
            for symbol in block:
                if np.random.rand() < e:
                    total_errors += 1  # ошибка
                total_symbols += 1  # символ
            
        # Средняя вероятность ошибки
        error_probabilities.append(total_errors / total_symbols)
    
    return error_probabilities

# Сбор данных
results = {p: simulate_errors(p, e, n_max, num_experiments) for p in p_values}

# Построение графиков
plt.figure(figsize=(10, 6))
for p, errors in results.items():
    plt.plot(range(1, n_max + 1), errors, marker='o', label=f'p = {p}')

plt.title('Зависимость вероятности ошибок от длины блока')
plt.xlabel('Длина блока (n)')
plt.ylabel('Вероятность ошибок')
plt.xticks(range(1, n_max + 1))
plt.legend()
plt.grid()
plt.show()
