import numpy as np

def count_num_range(numbers, a, b):
    # Фильтруем и подсчитываем числа в интервале [a +- b]
    in_interval = (numbers >= a - b) & (numbers <= a + b)
    return np.count_nonzero(in_interval) 

def count_num_interval(numbers, a, b):
    in_interval = (numbers >= a) & (numbers <= b)
    return np.count_nonzero(in_interval) 