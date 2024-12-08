def project_point_on_line():
    # Ввод координат точки A
    x1, y1 = map(float, input("Введите координаты точки A (x1 y1): ").split())
    
    # Ввод координат точки B
    x2, y2 = map(float, input("Введите координаты точки B (x2 y2): ").split())
    
    # Ввод координат произвольной точки P
    xp, yp = map(float, input("Введите координаты произвольной точки P (xp yp): ").split())
    
    # Вектор AB
    AB_x = x2 - x1
    AB_y = y2 - y1
    
    # Вектор AP
    AP_x = xp - x1
    AP_y = yp - y1
    
    # Длина вектора AB в квадрате
    AB_norm_sq = AB_x**2 + AB_y**2
    
    # Вычисляем скалярное произведение AP и AB
    dot_product_AP_AB = AP_x * AB_x + AP_y * AB_y
    
    # Длина проекции вектора AP на вектор AB
    projection_length = dot_product_AP_AB / AB_norm_sq
    
    # Координаты проекции точки P на прямую
    proj_x = x1 + projection_length * AB_x
    proj_y = y1 + projection_length * AB_y
    
    # Выводим результат
    print(f"Проекция точки P на прямую, проходящую через A и B: ({proj_x:.3f}, {proj_y:.3f})")

# Запуск функции
project_point_on_line()
