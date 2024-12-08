import numpy as np
import matplotlib.pyplot as plt

class Answer:
    def __init__(self):
        self.matrix = []
        self.test = 0

    def add(self, massive):
        self.matrix.append(massive)
        self.test += 1

    def print_test(self, massive):
        print(f"Тест {self.test}")
        for i in range(len(massive)-1):
            print(f"Касса {i+1}: {massive[i]:.3f} поситителей.")
        print(f"Упущено клеентов {massive[-1]:.3f}.")
        print(f"Количество клиентов {sum(massive):.3g}. \n")
    
    def print_answer(self):
        transposed_matrix = np.array(self.matrix).T
        # Вычисляем среднее значение по каждой строке
        mean_values = np.mean(transposed_matrix, axis=1)

        # Находим максимальное значение в каждой строке
        max_values = np.max(transposed_matrix, axis=1)
        min_values = np.min(transposed_matrix, axis=1)
        # Вычисляем разницу между максимальным и средним значением для каждой строки
        differences = max_values - mean_values


        for i in range(len(transposed_matrix)-1):
            print(f"Касса {i+1}: Минимальное = {min_values[i]}, Среднее = {mean_values[i]:.3f} +-{differences[i]:.3f}, Максимальное = {max_values[i]}")
        print(f"Упущено клиентов:  Минимальное = {min_values[-1]}, Среднее = {mean_values[-1]:.3f} +-{differences[-1]:.3f}, Максимальное = {max_values[-1]}")
        print(f"Количество клиентов {sum(max_values)}")
        

    def print_parametr(self, N, a, work_time, T):
        print(f"Количество касс {N}, а={a}, время обслуживание {work_time} мин, время моделирования {T} мин")

    def _draw_func(self, a):
        # Создаем массив значений x
        x = np.linspace(0, 10, 400)  # 400 точек от -10 до 10

        # Вычисляем соответствующие значения f(x)
        y = a * np.exp(-a * x)

        # Создаем график
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label='f(x) = 1/a*exp(-ax)', color='blue')

        # Добавляем заголовок и метки осей
        plt.title('График функции f(x) = 1/a*exp(-ax)')
        plt.xlabel('x')
        plt.ylabel('f(x)')

        # Добавляем сетку и легенду
        plt.grid()
        plt.legend()

        # Показываем график
        plt.show(block=False)


    def _draw_statistic(self):
        transposed_matrix = np.array(self.matrix).T
        # Вычисляем среднее значение по каждой строке
        mean_values = np.mean(transposed_matrix, axis=1)

        # Находим максимальное значение в каждой строке
        max_values = np.max(transposed_matrix, axis=1)

        differences = max_values - mean_values
        # Создаем координаты для оси x
        x = np.arange(len(mean_values))  # Индексы столбцов

        # Устанавливаем ширину столбцов
        width = 0.35

        # Создаем график
        plt.figure(figsize=(8, 6))

        # Рисуем столбцы для средних значений
        plt.bar(x, mean_values, width, label='Среднее', color='blue')

        # # Рисуем столбцы для максимальных значений, начиная с верхней части столбцов средних значений
        plt.bar(x, differences, width, label='максимальное', bottom=mean_values, color='orange')

        # Добавляем заголовок и метки осей
        plt.title('Накладывающиеся средние и максимальные значения по столбцам')
        plt.xlabel('Индекс столбца')
        plt.ylabel('Значение')

        # Добавляем легенду и сетку
        plt.legend()
        plt.grid()

        # Устанавливаем метки по оси x
        massive_name = [f'касса {i+1}' for i in range(len(mean_values)-1)]
        massive_name.append("упущены")

        plt.xticks(x, massive_name)

        # Показываем график
        plt.tight_layout()
        plt.show()


    def draw_graph(self, a):
        self._draw_func(a)
        self._draw_statistic()


    