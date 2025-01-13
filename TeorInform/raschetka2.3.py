from itertools import product

# Данные
X = {0: "a", 1: "b", 2: "c"}
n = 46

# Вероятности появления символов
P = [n / 140, n / 140, 1 - n / 70]

# Проверяем корректность вероятностей
if not all(0 <= p <= 1 for p in P) or abs(sum(P) - 1) > 1e-6:
    raise ValueError("Вероятности некорректны")

# Генерация всех возможных кодов фиксированной длины
fixed_length = 2  # Длина ансамбля которого мы хотим закодировать
binary_length = 3 # Длина в бинарного кода которым мы пытаемя закодировать



symbols = list(X.values())

codes = list(product(symbols, repeat=fixed_length))

# Вычисление вероятности для каждого кода и его длины
code_probabilities = []
for code in codes:
    probability = 1
    for symbol in code:
        probability *= P[symbols.index(symbol)]
    code_probabilities.append((code, len(code), probability))

# Сортировка по возрастанию вероятностей
code_probabilities.sort(key=lambda x: x[2])


# Вывод в одной строке
print("Коды с вероятностями и двоичное кодирование символов:")
i = 0
sum_Pe = 0
for code, length, probability in code_probabilities:
    if i < len(X)** fixed_length - 2**binary_length:
        sum_Pe += probability
    print(f"Код: {''.join(code)} |  {probability:.6f} | { format(i, f'0{binary_length}b')[-binary_length:]}")
    i +=1


print(f"Вероятность ошибки {sum_Pe}")
