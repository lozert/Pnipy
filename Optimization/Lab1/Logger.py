class Logger:
    def __init__(self, initial_string=""):
        self.string = initial_string
        self.i = 0
    def __call__(self, a, b, eps, part_string=""):
        self.i+= 1
        self.string += f" {self.i} a = {a:^7.3f} | b = {b:^10.3f} | b-a = {b-a:^10.3f} | eps = {eps:^7.3f} | {part_string}\n"
        return self.string
    
    def get_string(self):
        return self.string