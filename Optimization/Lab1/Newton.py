import numpy as np
import matplotlib.pyplot as plt
from FuncDerewative import FunctionWithDerivatives, func
from Logger import Logger



# Создаем объект класса для нашей функции
f = FunctionWithDerivatives(func)
logger = Logger()
# Метод Ньютона
def newton_method(x0, eps=1e-6, max_iter=100):
    for i in range(max_iter):
        f_prime = f.df(x0)
        f_double_prime = f.d2f(x0)
        
        if f_double_prime == 0:
            print("Вторая производная равна нулю, метод остановлен.")
            return None
        
        x1 = x0 - f_prime / f_double_prime
        

        if abs(x1 - x0) < eps and abs(f.f(x1)- f.f(x0)) < eps:
            print(f'Сходимость достигнута за {i+1} итераций')
            print(f"Answer {x1}")
            return x1
        
        # Обновляем x0 для следующей итерации
        logger(x0, x1, eps)
        x0 = x1
    
    print("Достигнуто максимальное число итераций")
    return x0

# Задаем начальную точку
x0 = 4    

# Запускаем метод Ньютона
min_x = newton_method(x0)
print(logger.get_string())

if min_x is not None:
    print(f'Найденная точка минимума: x = {min_x}, f(x) = {f.f(min_x)}')

    # Визуализация
    x_vals = np.linspace(0, 3, 400)
    y_vals = f.f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.scatter(min_x, f.f(min_x), color='red', label='Минимум', zorder=5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Минимизация методом Ньютона')
    plt.grid(True)
    plt.show()
