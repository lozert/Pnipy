from utils.Constructor import constuct_str
import random

massiv_z = ["солнечно", "облачно", "дождь"]
massiv_x = ["температура низкая", "Температура высокая", "Влажность низкая", "Влажность высокая", "Давление низкое", "Давление высокое"]




massiv_mnoz = [[[0.2, 0.6, 0.2], [0.1, 0.7, 0.2], [0.05, 0.15, 0.8]],
               [[0.8, 0.15, 0.05],[0.35, 0.5, 0.15], [0.1, 0.3, 0.6]],
               [[0.7, 0.2, 0.1], [0.25, 0.6, 0.15], [0.1, 0.5, 0.4]],
               [[0.2, 0.5, 0.3], [0.1, 0.3, 0.6], [0, 0.2, 0.8]],
               [[0.1, 0.6, 0.3], [0.15, 0.2, 0.65], [0.1, 0.2, 0.7]],
               [[0.75, 0.2, 0.05], [0.5, 0.4, 0.1], [0.3, 0.5, 0.2]]]


def rand(massiv):
    rnd = random.random()  
    sum_prob = 0  
    for index in range(len(massiv)):
        sum_prob += massiv[index] 
        if rnd <= sum_prob:  
            return index 
    return len(massiv) - 1  

i = 0

new_sost = 0
while True:
    
    if i == 0:
        x = int(input(f"Введите номер входных данных: {constuct_str(massiv_x)}"))
        z = int(input(f"Введите номер состояния: {constuct_str(massiv_z)}"))
        massiv = massiv_mnoz[x][z]
        new_sost = rand(massiv)
        print(f"Ответ: С состояния {massiv_z[z]} --> {massiv_z[new_sost]} \nС вероятностью {massiv[new_sost]}\n")
        i+=1

    else:
        x = int(input(f"Введите номер входных данных: {constuct_str(massiv_x)}"))
        massiv = massiv_mnoz[x][new_sost]
        new_sost1 = new_sost
        new_sost = rand(massiv)
        print(f"new sost {new_sost}")
        print(f"Ответ: С состояния {massiv_z[new_sost1]} --> {massiv_z[new_sost]} \nС вероятностью {massiv[new_sost]}\n")
