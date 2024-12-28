import math

def H(probabilities):
    """Вычисляет энтропию для списка вероятностей"""
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def HNderM(PNM, PNderM):
    sum = 0 
    for i in range(len(PNM)):
        for j in range(len(PNM[0])):
            if PNderM[i][j] > 0:  # Проверяем, что значение больше 0
                sum -= PNM[i][j] * math.log2(PNderM[i][j])
    
    return sum

if __name__ == "__main__":
    p = [5/140, 5/140, 1-5/70]
    print(H(p))