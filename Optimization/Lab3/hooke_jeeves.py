import numpy as np

def hooke_jeeves_modified(f, x_start, alpha=2, lambd=1.0, tol=1e-6, max_iter=100000):
    """
    Модифицированный метод Хука-Дживса для минимизации функции нескольких переменных.
    
    Параметры:
    f        - минимизируемая функция
    x_start  - начальная базисная точка
    alpha    - ускоряющий множитель (обычно alpha = 2)
    lambd    - начальный шаг исследующего поиска (λ^(0))
    tol      - требуемая точность
    max_iter - максимальное количество итераций
    """
    
    def explore_neighborhood(x_b, lambd):
        """Вычисляет точки окрестности и возвращает минимальную точку и значение функции."""
        n = len(x_b)
        neighborhood = [np.copy(x_b)]
        
        # Создание точек окрестности
        for i in range(n):
            x_forward = np.copy(x_b)
            x_backward = np.copy(x_b)
            x_forward[i] += lambd
            x_backward[i] -= lambd
            neighborhood.append(x_forward)
            neighborhood.append(x_backward)

        # Находим точку с минимальным значением функции
        f_values = [f(x) for x in neighborhood]
        min_index = np.argmin(f_values)
        return neighborhood[min_index], f_values[min_index]

    x_b = np.copy(x_start)
    iteration = 0
    fails = 0

    while iteration < max_iter:
        # Поиск минимального значения функции в окрестности
        x_star, f_star = explore_neighborhood(x_b, lambd)

        # Если улучшения нет, уменьшаем шаг исследующего поиска
        if f(x_star) >= f(x_b):
            fails += 1
            lambd = lambd / (2 * np.exp(fails))
        else:
            # Обновляем базисную точку в направлении x_star - x_b
            direction = x_star - x_b
            x_b = x_b + alpha * direction
            fails = 0  # Обнуляем счётчик неудач

        # Проверка условия остановки
        if lambd < tol:
            print("РАзница между знач ф меньше погрешности")
            break

        iteration += 1

    return x_b, f(x_b), iteration

# Пример использования

def func(x):
    return x[0] + 2*x[1] + 4 * np.sqrt(1 + x[0]**2 +x[1]**2)

x_start = np.array([1.0, 1.0])
result, f_min, iter = hooke_jeeves_modified(func, x_start)

print("Точка минимума:", result)
print("Минимальное значение функции:", f_min)
print("Итераций: ", iter )