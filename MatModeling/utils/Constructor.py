
def constuct_str(massiv):
    string = ""
    for i in range(len(massiv)):
        string += f"{i}-{massiv[i]} "
    return string + "\n"