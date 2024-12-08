import numpy as np


class FunctionWithDerivatives:
    def __init__(self, func):
        self.func = func
    
    def f(self, x):
        """Значение функции f(x)"""
        return self.func(x)
    
    def df(self, x, h=1e-6):
        """Численное вычисление первой производной f'(x) с помощью конечных разностей"""
        return (self.func(x + h) - self.func(x - h)) / (2 * h)
    
    def d2f(self, x, h=1e-6):
        """Численное вычисление второй производной f''(x) с помощью конечных разностей"""
        return (self.func(x + h) - 2*self.func(x) + self.func(x - h)) / (h ** 2)
    

func = lambda x : (x**2 ) / 2 - np.cos(x)