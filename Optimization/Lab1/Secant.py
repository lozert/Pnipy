import numpy as np
import matplotlib.pyplot as plt
from Logger import Logger
from FuncDerewative import FunctionWithDerivatives, func

f = FunctionWithDerivatives(func)
logger = Logger()

def secant_method(x0, x1, eps=1e-6, max_iter=100):
    for i in range(max_iter):
        # Вычисляем значения производной функции в точках x0 и x1
        f_prime_x0 = f.df(x0)
        f_prime_x1 = f.df(x1)

        # Проверяем, чтобы знаменатель не был нулём
        if f_prime_x1 - f_prime_x0 == 0:
            print("Деление на ноль, метод остановлен.")
            return None

        
        x2 = x1 - f_prime_x1 * (x1 - x0) / (f_prime_x1 - f_prime_x0)

        # Проверяем условие сходимости
        if abs(x2 - x1) < eps:
            print(f'Сходимость достигнута за {i+1} итераций')
            return x2

        # Обновляем точки для следующей итерации
        logger(x0, x1, eps, f"f'(x0) = {f.df(x0):.3f} | f'(x1) = {f.df(x1):.3f}")
        x0 = x1
        x1 = x2

    print("Достигнуто максимальное число итераций")
    return x1

# Задаем начальные точки
x0 = 0
x1 = 3

# Запускаем метод секущих
min_x = secant_method(x0, x1)
print(logger.get_string())

if min_x is not None:
    print(f'Найденная точка минимума: x = {min_x}, f(x) = {f.f(min_x)}')

    # Визуализация
    x_vals = np.linspace(x0, x1, 400)
    y_vals = f.f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.scatter(min_x, f.f(min_x), color='red', label='Минимум', zorder=5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Минимизация методом секущих (ломаной)')
    plt.grid(True)
    plt.show()
