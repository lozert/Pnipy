import numpy as np
import matplotlib.pyplot as plt
from Logger import Logger
from FuncDerewative import func

gs = 0.618
x_values = []
y_values = []
x1_values = []
y1_values = []

def golden_section(a, b, eps=1e-6):
    golden_logger = Logger()
    lam = a + (1 - gs) * (b - a)
    mi = a + gs * (b - a)


    while (b - a > eps):
        if func(lam) < func(mi):
            b = mi
            mi = lam
            lam = a + (1 - gs)*(b - a)
        else:
            a = lam
            lam = mi
            mi = a + gs * (b - a)

        golden_logger(a, b, eps, f"lam = {lam:.3f} | mi = {mi:.3f}")
        x_values.append(lam)
        y_values.append(func(lam))
        x1_values.append(mi)
        y1_values.append(func(mi))

    print(f"Answer: {(b+a)/2}")
    return golden_logger.get_string()

a, b = 0, 3

result = golden_section(a, b)
print(result)



# Построение графика
x = np.linspace(a, b, 400)
y = func(x)
plt.plot(x, y, label='func(x)')
plt.scatter(x_values, y_values, color='red', label='Golden Section Points')
plt.scatter(x1_values, y1_values, color='green')
plt.xlabel('x')
plt.ylabel('func(x)')
plt.legend()
plt.title('Golden Section Method')
plt.grid(True)
plt.show()