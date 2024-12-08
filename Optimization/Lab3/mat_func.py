import numpy as np

def hooke_jeeves(func, x0, constraints=None, step_size=0.1, tol=1e-6, max_iter=1000):
    """
    Реализация метода Хука-Дживса с учётом штрафной функции для учета ограничений.

    :param func: Целевая функция для минимизации.
    :param x0: Начальная точка (массив с \( n \) элементами).
    :param constraints: Список функций-ограничений (g_i(x) <= 0 или g_i(x) == 0).
    :param step_size: Начальный размер шага.
    :param tol: Точность для критерия завершения.
    :param max_iter: Максимальное количество итераций.
    :return: Словарь с результатами оптимизации.
    """
    import itertools
    import numpy as np

    # Штрафная функция
    def penalty_function(x, A=1e6, q=2):
        penalty = 0
        if constraints:
            for g in constraints:
                violation = g(x)
                if violation > 0:  # Учитываем только нарушения
                    penalty += A * (violation ** q)
        return penalty

    # Обёртка для целевой функции с учетом штрафной функции
    def augmented_func(x, A=1e6, q=2):
        return func(x) + penalty_function(x, A, q)

    # Инициализация
    x_current = np.array(x0)
    n = len(x0)  # Размерность пространства
    iteration = 0

    while iteration < max_iter:
        iteration += 1
        # Генерация всех точек в окрестности текущей точки
        offsets = np.array(list(itertools.product([-1, 0, 1], repeat=n))) * step_size
        neighbors = x_current + offsets  # Все соседние точки

        # Находим точку с минимальным значением функции
        values = np.array([augmented_func(x) for x in neighbors])
        min_index = np.argmin(values)
        x_min = neighbors[min_index]
        f_min = values[min_index]

        # Проверяем сходимость
        if np.linalg.norm(x_current - x_min) < tol:
            break

        # Обновляем текущую точку, если найдена более лучшая точка
        if f_min < augmented_func(x_current):
            x_current = x_min
        else:
            # Уменьшаем шаг, если улучшений не найдено
            step_size *= 0.5

    # Результаты
    return {
        "x": x_current,            # Найденная оптимальная точка
        "fun": augmented_func(x_current),  # Значение функции в оптимальной точке
        "nit": iteration,          # Число итераций
        "success": step_size < tol  # Условие успешного завершения
    }




def nelder_mead_balanced(func, constraints, x0, max_iter=1000, tol=1e-6, penalty_weight=1e3):
    """
    Реализация метода Нелдера-Мида с балансировкой между целевой функцией и штрафной функцией.
    
    :param func: Целевая функция для минимизации.
    :param constraints: Список функций-ограничений (g_i(x) <= 0 или g_i(x) == 0).
    :param x0: Начальная точка.
    :param max_iter: Максимальное число итераций.
    :param tol: Точность завершения.
    :param penalty_weight: Вес штрафной функции в итоговой функции.
    :return: Найденная точка и значение функции.
    """
   

    # Баланс штрафа: функция ошибок + штрафная составляющая
    def error_function(x, A=1.0, q=2):
        error = 0
        for g in constraints:
            violation = g(x)
            # Ошибка учитывается по модулю: как для нарушений, так и для пересечений
            error += A * np.abs(violation) ** q
        return error

    # Итоговая функция для минимизации
    def balanced_function(x):
        return func(x) + penalty_weight * error_function(x)

    # Инициализация симплекса
    n = len(x0)
    simplex = [x0]
    for i in range(n):
        vertex = x0[:]
        vertex[i] += 1.0  # Начальные смещения по каждой координате
        simplex.append(vertex)
    simplex = np.array(simplex)

    # Сортировка симплекса по значению функции
    def sort_simplex(simplex):
        return sorted(simplex, key=lambda x: balanced_function(x))

    # Коэффициенты метода Нелдера-Мида
    alpha, gamma, rho, sigma = 1.0, 2.0, 0.5, 0.5

    # Основной цикл оптимизации
    iteration = 0
    while iteration < max_iter:
        # Сортировка вершин симплекса
        iteration += 1
        simplex = sort_simplex(simplex)
        f_values = [balanced_function(x) for x in simplex]

        # Проверка на сходимость (разница между наилучшей и наихудшей точкой)
        if np.abs(f_values[-1] - f_values[0]) < tol:
            break

        # Центр тяжести, исключая наихудшую точку
        centroid = np.mean(simplex[:-1], axis=0)

        # Отражение
        x_reflected = centroid + alpha * (centroid - simplex[-1])
        f_reflected = balanced_function(x_reflected)

        if f_values[0] <= f_reflected < f_values[-2]:
            simplex[-1] = x_reflected  # Заменяем наихудшую точку отражением
            continue

        # Расширение
        if f_reflected < f_values[0]:
            x_expanded = centroid + gamma * (x_reflected - centroid)
            f_expanded = balanced_function(x_expanded)
            if f_expanded < f_reflected:
                simplex[-1] = x_expanded
            else:
                simplex[-1] = x_reflected
            continue

        # Сжатие
        x_contracted = centroid + rho * (simplex[-1] - centroid)
        f_contracted = balanced_function(x_contracted)
        if f_contracted < f_values[-1]:
            simplex[-1] = x_contracted
            continue

        # Редукция (сжимаем все точки к лучшей точке)
        best_point = simplex[0]
        simplex = np.array([best_point + sigma * (x - best_point) for x in simplex])

    # Возвращаем результаты
    best_point = simplex[0]
    best_value = balanced_function(best_point)
    return {
        "x": best_point,
        "fun": best_value,
        "error": error_function(best_point),
        "nit": iteration,
        "success": iteration < max_iter
    }

# Пример использования
def target_func(x):
    return x[0] + 2 * x[1] + 4 * np.sqrt(1 + x[1]**2 + x[0]**2)

def constraint1(x):
    return 2*x[0] + 8 * x[1] - 10



if __name__ == "__main__":
    # Начальная догадка
    # Начальная точка
    x0 = [1, 1]

    
  

    result = nelder_mead_balanced(target_func, [constraint1], x0)
    print("Результаты оптимизации:")
    print(f"Оптимальная точка: {result['x']}")
    print(f"Минимальное значение функции: {result['fun']}")
    print(f"Значение функции ошибки: {result['error']}")
    print(f"Количество итераций: {result['nit']}")
    print(f"Успешное завершение: {result['success']}\n")

    result = nelder_mead_balanced(target_func, [], x0)
    print("Результаты оптимизации:")
    print(f"Оптимальная точка: {result['x']}")
    print(f"Минимальное значение функции: {result['fun']}")
    print(f"Значение функции ошибки: {result['error']}")
    print(f"Количество итераций: {result['nit']}")
    print(f"Успешное завершение: {result['success']}\n")
