""" Моделирование кассового аппарата """

from utils import mat_func, construct_answer
import numpy as np
import time
import argparse


parser = argparse.ArgumentParser(description="Self-paced contrastive learning on unsupervised re-ID")
parser.add_argument('-c', '--case', type=int, default=0)

args = parser.parse_args()

T = 10 * 60 # время моделирования
if args.case == 1:
    N = 10 
    a = 4
    work_time = 1
elif args.case == 2:
    N = 5
    a = 0.65
    work_time = 2
elif args.case == 3:
    N = 2 
    a = 0.2 
    work_time = 2.2

inv_a =  - 1 / a

# Количество моделирование дней
count_iter = 1000
count_test = 4

# TODO: выводить сколько клинетов было, в каком соотношении их было упущено 

answer = construct_answer.Answer()
start = time.time()

for j in range(count_test):
    count_complite = np.zeros(N+1)
    time_queue = np.zeros(N)
    # Моделирование count_iter дней
    for i in range(count_iter):
        
        current_time = 0
        
        #Моделирование одного рабочего дня
        while current_time < T:
            next_person = mat_func.gen_exp(inv_a)

            for index in range(len(time_queue)):        
                if time_queue[index] < next_person:
                    count_complite[index] += 1
                    
                    time_queue = np.array([max(0, item - next_person) for item in time_queue ])
                    time_queue[index] = work_time 
                    break
                
                if index == N - 1:
                    count_complite[-1] += 1
            current_time += next_person

    avarage_massive = count_complite / count_iter
    answer.add(avarage_massive)
    answer.print_test(avarage_massive)


end = time.time()
print(f"Время выполнения {(end-start):.3f} сек")
answer.print_parametr(N, a, work_time, T)
answer.print_answer()
answer.draw_graph(a)

    
