massiv_x = ["Отдать заряд", "Получить заряд", " Покой"]
massiv_y = ["Синий индикатор", "Зелёный индикатор", "Ничего не горит", "Красный индикатор"]
massiv_z = ["Повербанк разряжается", "Повербанк заряжается", "Покой", "Отсутвие заряда"]

matrix_state = [[0,0,0,2],
                [1,1,1,1],
                [2,2,2,2]]

matrix_output = [[0,0,0,3],
                 [1,1,1,1],
                 [2,2,2,2]]

def constuct_str(massiv):
    string = ""
    for i in range(len(massiv)):
        string += f"{i}-{massiv[i]} "
    return string

x = int(input(f"Введи номер входного сигнала ({constuct_str(massiv_x)})\n"))
z = int(input(f"Введите состояние {constuct_str(massiv_z)}\n"))

new_state = matrix_state[x][z]
output = matrix_output[x][z]

print(f"Входной сигнал '{massiv_x[x]}'")
print(f"Новое состояние '{massiv_z[new_state]}'")
print(f"Выходной сигнал '{massiv_y[output]}'")

