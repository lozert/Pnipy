import numpy as np
import ast

class DataProcessor:
    def __init__(self, functions, range_str):
        self.functions = functions
        self.range_str = range_str

    def process_data(self):
        y_values = []
        num = 300
        try:
            start, stop, num = map(ast.literal_eval, self.range_str.split(','))
            num +=2
        except:
            start, stop = map(ast.literal_eval, self.range_str.split(','))
        x_range = np.linspace(start, stop, num)

        for func in self.functions:
            text_function = func.text()
            y_values.append(eval(f"{text_function}", {"x": x_range, "np": np}))
        
        return x_range, y_values
