import numpy as np
import matplotlib.pyplot as plt

# Целевая функция
def f(x):
    return x[0] + 2 * x[1] + 4 * np.sqrt(1 + x[1]**2 + x[0]**2)

# Ограничение
def penalty_func(x):
    return  2*x[0] + 8 * x[1] - 10

# Штрафная функция
def penalty_function(x, A=2, q=3):
    violation = penalty_func(x)
    return A * (violation ** q) if violation > 0 else 0

# Объединенная функция: целевая + штрафная
def augmented_function(x, A=2, q=2):
    return f(x) + penalty_function(x, A, q)

# Метод Нелдера-Мида с учетом штрафа
def nelder_mead_with_penalty(func, x0, max_iter=1000, tol=1e-6, A=0.5, q=2):
    """
    Реализация метода Нелдера-Мида с учетом штрафной функции.

    :param func: Целевая функция (без штрафа).
    :param x0: Начальная точка.
    :param max_iter: Максимальное количество итераций.
    :param tol: Точность завершения.
    :param A: Вес штрафа.
    :param q: Степень штрафа.
    :return: Найденная точка, значение функции, количество итераций, история симплексов.
    """
    # Коэффициенты метода Нелдера-Мида
    alpha, gamma, rho, sigma = 1.0, 2.0, 0.5, 0.5

    # Инициализация симплекса
    n = len(x0)
    simplex = [x0]
    shift = 0.5
    for i in range(n):
        vertex = np.copy(x0)
        vertex[i] += shift
        simplex.append(vertex)
    simplex = np.array(simplex)

    simplex_history = [np.array(simplex)]
    iteration = 0

    # Основной цикл оптимизации
    while iteration < max_iter:
        iteration += 1

        # Сортировка вершин симплекса по значению объединенной функции
        simplex = sorted(simplex, key=lambda x: augmented_function(x, A, q))
        f_values = [augmented_function(x, A, q) for x in simplex]

        # Проверка на сходимость
        if np.abs(f_values[-1] - f_values[0]) < tol:
            print("Закончили")
            break

        # Центр масс, исключая наихудшую точку
        centroid = np.mean(simplex[:-1], axis=0)

        # Отражение
        x_reflected = centroid + alpha * (centroid - simplex[-1])
        f_reflected = augmented_function(x_reflected, A, q)

        if f_values[0] <= f_reflected < f_values[-2]:
            simplex[-1] = x_reflected
        elif f_reflected < f_values[0]:
            # Расширение
            x_expanded = centroid + gamma * (x_reflected - centroid)
            f_expanded = augmented_function(x_expanded, A, q)
            simplex[-1] = x_expanded if f_expanded < f_reflected else x_reflected
        else:
            # Сжатие
            x_contracted = centroid + rho * (simplex[-1] - centroid)
            f_contracted = augmented_function(x_contracted, A, q)
            if f_contracted < f_values[-1]:
                simplex[-1] = x_contracted
            else:
                # Редукция
                best_point = simplex[0]
                simplex = np.array([best_point + sigma * (x - best_point) for x in simplex])

        simplex_history.append(np.array(simplex))

    return simplex[0], f_values[0], iteration, simplex_history


# Начальная точка
x0 = np.array([1.0, 1.0])

# Запуск метода Нелдера-Мида
minimum, f_min, iterations, simplex_history = nelder_mead_with_penalty(f, x0)

print("Минимум функции с учетом штрафа:", minimum)
print("Значение функции в минимуме (с учетом штрафа):", f_min)
print("Количество итераций:", iterations)

# Построение графика
x_range = np.linspace(-1, 2, 200)
y_range = np.linspace(-1, 2, 200)
X, Y = np.meshgrid(x_range, y_range)
Z = X + 2 * Y + 4 * np.sqrt(1 + Y**2 + X**2)



plt.figure(figsize=(10, 8))
plt.contour(X, Y, Z, levels=50, cmap="viridis")
plt.colorbar(label="f(x)")

# Отображение симплексов
for simplex in simplex_history:
    plt.plot(simplex[:, 0], simplex[:, 1], 'k-', alpha=0.4)
    plt.plot(simplex[:, 0], simplex[:, 1], 'ko', markersize=3)

x_line = np.linspace(-2, 2, 200)
y_line = -(2* x_line + 10) / 8
plt.plot(x_line, y_line, 'r--', label='Ограничение: $x_1 + 8x_2 + 5 = 0$')

# Точки минимума
plt.plot(x0[0], x0[1], 'bo', label='Начальная точка (x0)')
plt.plot(minimum[0], minimum[1], 'ro', label='Минимум функции с учетом штрафа')

plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("Минимизация функции методом Нелдера-Мида с учетом штрафа")
plt.legend()
plt.show()
