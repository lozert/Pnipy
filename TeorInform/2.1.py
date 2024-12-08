import numpy as np
from scipy.optimize import fsolve

# Определяем функцию
def equation(p):
    term1 = -2 * p**2 * np.log(p) if p > 0 else np.inf
    term2 = -p * np.log(p) if p > 0 else np.inf
    term3 = (p**2 + p - 1) * np.log(-p**2 / 2 - p / 2 + 1 / 2) if (-p**2 / 2 - p / 2 + 1 / 2) > 0 else np.inf
    
    return term1 + term2 + term3

# Численное решение уравнения
p_initial_guess = 0.5  # Начальное приближение
solution = fsolve(equation, p_initial_guess)
print(solution)
