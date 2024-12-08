import numpy as np


def gen_exp(inv_a):
    U = np.random.rand()  # Генерация одного случайного числа
    return  inv_a * np.log(1 - U)

if __name__ == "__main__":
    print(gen_exp(2))