import numpy as np

CODING_BITS = 8

class Table:
    def __init__(self, description=None, num_letter=None, code_symbol=None, bits=None):
        self.description = description
        self.num_letter = num_letter
        self.code_symbol = code_symbol
        self.bits = bits

    def __repr__(self):
        description = str(self.description).ljust(6)
        num_letter = str(self.num_letter).ljust(3)
        code_symbol = str(self.code_symbol).ljust(14)
        bits = str(self.bits).ljust(4)
        return f"| {description} | {num_letter} | {code_symbol} | {bits}"

# Создаем список данных
data = {}
data[0] = Table(0, 0, 0, 0)

input_text = "IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN"

def indesc(item):
    """Функция для поиска индексов элементов в словаре, соответствующих заданному описанию."""
    match_indices = []
    for key, value in data.items():
        if item == str(value.description):
            match_indices.append(key)
    return match_indices

def find_max_subword(index_letter):
    """Функция для нахождения максимальной подстроки, начиная с заданного индекса."""
    if index_letter == len(input_text) - 1:
        return input_text[index_letter]

    max_sub_word = input_text[index_letter:index_letter + 2]
    len_letter = 0

    while indesc(max_sub_word):
        if index_letter + len_letter + 2 >= len(input_text):
            break
        max_sub_word += input_text[index_letter + len_letter + 2]
        len_letter += 1

    return max_sub_word

def to_binary_with_bits(number, num_bits):
    """Функция для преобразования числа в бинарную строку с заданным количеством бит."""
    binary_str = bin(number)[2:]
    binary_str = binary_str.zfill(num_bits)
    return binary_str

index = 0
dict_index = 0

while index < len(input_text):
    # Проверка, что элемент есть в словаре
    if indesc(input_text[index]):
        letter = find_max_subword(index)
        
        if len(letter) == 1:
            num_letter = indesc(letter)[0]
        else:
            num_letter = indesc(letter[:-1])[0]

        ceil = int(np.ceil(np.log2(dict_index)))
        if num_letter == dict_index:
            
            code_symbol = "0" * ceil + f"bin({input_text[index]})"
            bits = ceil + len(input_text[index]) * CODING_BITS
            data[dict_index + 1] = Table(letter, 0, code_symbol, bits)
        else:
            data[dict_index + 1] = Table(letter, num_letter, to_binary_with_bits(num_letter, ceil), ceil)

        if len(letter) == 1:
            index += 1
        else:
            index += len(letter) - 1

        dict_index += 1
    else:
        symbol = input_text[index]
        ceil = 0
        if index != 0:
            ceil = int(np.ceil(np.log2(index)))
        
        code_symbol = "0" * ceil + f"bin({input_text[index]})"
        bits = ceil + len(input_text[index]) * CODING_BITS
        data[dict_index + 1] = Table(symbol, 0, code_symbol, bits)

        index += 1
        dict_index += 1

sum_bits = 0
for key, value in data.items():
    print(f"{key}: {value}")
    sum_bits += value.bits

print(f"Total bits: {sum_bits}")
