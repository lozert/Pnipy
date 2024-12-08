import numpy as np

def func(x, y):
    return x + 2 * y + 4 * np.sqrt(1 + x**2 + y**2)

def grad_func(x, y):
    grad_x = 1 + (4 * x) / np.sqrt(1 + x**2 + y**2)
    grad_y = 2 + (4 * y) / np.sqrt(1 + x**2 + y**2)
    return grad_x, grad_y

def gradient_descent(func, grad_func, x_init, y_init, learning_rate=0.1, tolerance=1e-6, max_iters=1000):
    x, y = x_init, y_init
    count_iter = 0
    for i in range(max_iters):
        count_iter +=1
        grad_x, grad_y = grad_func(x, y)
        x_new = x - learning_rate * grad_x
        y_new = y - learning_rate * grad_y
        
        # Проверка на сходимость
        if abs(func(x_new, y_new) - func(x, y)) < tolerance:
            break
        
        x, y = x_new, y_new
    return x, y, count_iter

# Начальные значения
x_init, y_init = 0.0, 0.0

# Оптимизация
optimal_x, optimal_y, count_iter = gradient_descent(func, grad_func, x_init, y_init)

print(f"Оптимальные значения: x = {optimal_x}, y = {optimal_y}")
print(f"Количество итераций {count_iter}")