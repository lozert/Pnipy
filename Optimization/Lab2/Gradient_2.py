import numpy as np
from matplotlib import pyplot as plt

# пропишем функцию потерь
def objective(w1, w2):
    return np.sin(w1) + np.cos(w2)
 
# а также производную по первой
def partial_1(w1):
    return np.cos(w1)
 
# и второй переменной
def partial_2(w2):
  return -np.sin(w2)


w1, w2 = 1.4, -0.3
 
# количество итераций
iter = 100
learning_rate = 0.05

w1_list, w2_list, l_list = [], [], []

# в цикле с заданным количеством итераций
for i in range(iter):

  w1_list.append(w1)
  w2_list.append(w2)

  l_list.append(objective(w1, w2))
 
  par_1 = partial_1(w1)
  par_2 = partial_2(w2)
 
  w1 = w1 - learning_rate * par_1
  w2 = w2 - learning_rate * par_2
 


w1, w2, objective(w1, w2)


fig = plt.figure(figsize = (14,12))
 
w1 = np.linspace(-5, 5, 1000)
w2 = np.linspace(-5, 5, 1000)
 
w1, w2 = np.meshgrid(w1, w2)
 
f = np.sin(w1) + np.cos(w2)
 
ax = fig.add_subplot(projection = '3d')
 
ax.plot_surface(w1, w2, f, alpha = 0.4, cmap = 'Blues')
 
 
ax.set_xlabel('w1', fontsize = 15)
ax.set_ylabel('w2', fontsize = 15)
ax.set_zlabel('f(w1, w2)', fontsize = 15)
 
# выведем путь алгоритма оптимизации
ax.plot(w1_list, w2_list, l_list, '.-', c = 'red')
 
plt.show()