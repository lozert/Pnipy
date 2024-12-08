# Исходные данные из таблицы
data = {
    "work": ["1→2", "1→3", "1→4", "2→5", "3→5", "3→6", "4→7", "5→8", "6→8", "6→9", "7->9","8→10", "9→10", "9→11", "10→12", "11→12"],
    "D_optim": [4, 3, 5, 4, 8, 4, 2, 6, 3, 3, 3, 5, 7, 4, 4, 3],
    "D_expected": [5, 5, 7, 4, 12, 6, 2, 8, 6, 4, 5, 8, 11, 4, 6, 5],
    "D_pessim": [6, 8, 8, 7, 14, 8, 3, 10, 9, 5, 8, 9, 14, 6, 8, 6]
}

print(len(data['work']))
print(len(data["D_optim"]))
print(len(data["D_expected"]))
print(len(data["D_pessim"]))

# Расчёт среднеквадратичного отклонения для каждого этапа
import numpy as np

# Формула для стандартного отклонения
sigma = [(pessim - optim) / 6 for optim, pessim in zip(data["D_optim"], data["D_pessim"])]

# Дисперсия для каждого этапа (квадрат отклонения)
variance = [s**2 for s in sigma]

# Общая дисперсия для критического пути
sigma_total = np.sqrt(sum(variance))

print(sigma_total)