import numpy as np
import random
from prettytable import PrettyTable

class Hamming:
    def __init__(self):
        self.massiv_code = []
        self.array_code = {}
    
    def coder(self, packets, error=False):
        for data in packets:
            new_code = self.expend_zerobits(data)
            value_bits = self.calculate_control_bits(new_code)
            code_with_controlbits = self.__expend_control_bits(new_code, value_bits)
            self.array_code["code"] = data
            self.array_code["code_without_error"] = code_with_controlbits
            self.massiv_code.append(self.array_code)
            self.array_code = {}

        return self.massiv_code

    def decoder(self, packets):
        for data in packets:
            index_error = 0
            value_bits = self.calculate_control_bits(data)
            bool_verify = self.__verify_control_bits(data, value_bits)
            if self.__is_any_false(bool_verify):
                index_error = self.calculate_error_index(bool_verify)
                self.array_code["index_error"] = index_error
                data = self.restore_sequence(data, index_error)
            self.array_code["restore_code"] = self.without_control_bits(data)
            self.massiv_code.append(self.array_code)
            self.array_code = {}

        return self.massiv_code

            
    def calculate_control_bits(self, code):
        value_bits = {}
        for index in range(len(code)):
            value_code = code[index]
            reverse_bit_index = ''.join(reversed(bin(index+1)))[:-2]
            for i in range(len(reverse_bit_index)):
                if reverse_bit_index[i] == '1':
                    try:
                        value_bits[i] = value_bits[i] + int(value_code)
                    except:
                        value_bits[i] = 0
        value_bits = {key: value % 2 for key, value in value_bits.items()}
        return value_bits
    
    def without_control_bits(self, code):
        new_code = ""
        i = 1
        while True:
            if self.is_integer_log2(i) and len(code) != 0:
                code = code[1:]
            else:
                try:
                    new_code += code[0]
                    code = code[1:]
                except IndexError:
                    break
            i +=1

        return new_code

    def restore_sequence(self, code, index_error):
        code_list = list(code)
        restore_value = np.abs(int(code_list[index_error-1]) - 1)
        code_list[index_error-1] = str(restore_value)
        return ''.join(code_list)
     
    def calculate_error_index(self, array):
        index_error = 0
        for index in range(len(array)):
            if array[index] == False:
                index_error += 2**index
        return index_error

    def __is_any_false(self, array):
        return any(item is False for item in array)
    
    def __verify_control_bits(self, code, contol_bits):
        code_list = list(code)
        result = []
        for key, value in contol_bits.items():
            if code_list[2**key-1] == str(value):
                result.append(True)
            else:
                result.append(False)
        return result
    
    def __expend_control_bits(self, code, control_bit):
        code_list = list(code)
        for key, value in control_bit.items():
            code_list[2**key-1] = str(value)
        return ''.join(code_list)
    
    def expend_zerobits(self, code):
        expended_code = ""
        i = 1
        while True:
            if self.is_integer_log2(i) and len(code) !=0:
                expended_code += "0"
            else:
                try:
                    expended_code += code[0]
                    code = code[1:]
                except IndexError:
                    break
            i += 1
        
        return expended_code
            
    def is_integer_log2(self, i):
        result = np.log2(i) / np.log2(2)
        return result.is_integer()


def append_error(code):
    index_error = random.randint(0, len(code))
    new_char = np.abs(int(code[index_error] )-1) 
    return code[:index_error] + str(new_char) + code[index_error + 1:]

def form_packets(codes):
    packets = []
    for code in codes:
        packets.append(code["code_with_error"])
    return packets

def calculate_code():
    hamming_coder = Hamming()
    hamming_decoder = Hamming()
    packets = []
    x = int(input("1 - слово, 2 - бинарка: "))
    if x == 1:
        text = input("Введите текст: ")
        packets = invert2bit(text)
    elif x == 2:
        bitcode = input("введите бинарную последовательность: ")
        packets = adjust_packets(bitcode)
    
    
    error = int(input("1- с ошибкой, 0 - без ошибки: "))
    result_coder = hamming_coder.coder(packets, error)
    
    array = []

    if error:
        for result in result_coder:
            result["code_without_error"] = result["code_without_error"]
            code_with_error = append_error(result["code_without_error"])
            result["code_with_error"] = code_with_error
            array.append(result)
    else:
        array = result_coder
    
    packets = form_packets(result_coder)
    result_decoder = hamming_decoder.decoder(packets)
    

    for index in range(len(result_decoder)):
        result_coder[index].update(result_decoder[index])

    return result_coder


def create_table(data):
    table = PrettyTable()

    # Берём заголовки из ключей первого словаря
    if data:
        table.field_names = data[0].keys()

    # Добавляем строки в таблицу
    for row in data:
        table.add_row(row.values())

    return table

def adjust_packets(bitcode, len_block=16):
    """Разбиение данные на блоки"""
    packets = [bitcode[i:i+len_block] for i in range(0, len(bitcode), len_block)]
    try:
        if len(packets[-1]) < len_block:
            packets[-2] = packets[-2] + packets[-1]
            packets.pop()
    except:
        pass
    return packets

def invert2bit(word, letter_in_block=4):
    string = ""
    array = []
    for i in range(len(word)):
        if i % letter_in_block == 0:
            if len(string) != 0:
                array.append(string)
                string = ""
            string += bin(ord(word[i]))[2:]
        else:
            string += bin(ord(word[i]))[2:]
    if string != "":
        array.append(string)
    return array


if __name__ == "__main__":
    hamming1 = Hamming()
    code = "1101"
    print(hamming1.calculate_control_bits(code))
    # print(create_table(calculate_code()))
    
