from PySide6.QtGui import QPen, QColor, QPainter, QPolygon
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import numpy as np


from scipy.stats import gaussian_kde, mode
import itertools

class PlotTriangle:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values
        self.min_x = np.min(x_values)
        self.max_x = np.max(x_values)

        self.calculate_min_max_y()
        

    def calculate_density(self, plotnost = 0.5):
        massiv = list(itertools.chain(*self.y_values))
        kde = gaussian_kde(massiv)
        new_ab = []
        data_set = {}
        value_set = set(massiv)

        for item in value_set:
            data_set[item] = kde(item)

        sorted(data_set.items(), key=lambda item: item[1], reverse=True)
        sum_value = 0 
        for key, value in data_set.items():
            if sum_value < plotnost:
                sum_value += value[0]
                new_ab.append(key)
            else:
                break

        self.data_set = data_set
        self.min_y = min(new_ab)
        self.max_y = max(new_ab)
        return new_ab
    
    def calculate_min_max_y(self):
        
        
        if np.all(np.array(self.y_values) > 0) or np.all(np.array(self.y_values) < 0):
            print("da")
            self.min_y = np.mean([np.min(data) for data in self.y_values]) 
            self.max_y = np.mean([np.max(data) for data in self.y_values])

            count_positive = np.sum(np.array(self.y_values) > 0) + 1
            count_negative = np.sum(np.array(self.y_values) < 0) + 1
            if count_negative / count_positive > 0.7:
                self.max_y = int(self.min_y * 0.1)
            if count_positive / count_negative > 0.7:
                self.min_y = - int(self.max_y * 0.1)
            print(self.min_y, self.max_y)
            
        else:

            new_ab = self.calculate_density()
            
            if np.abs(self.min_y) > np.std(np.array(new_ab)):
                self.min_y =  - np.std(np.array(new_ab))
            print(self.min_y)
            if self.min_y > - 2.0:
                self.min_y = -2
            if self.max_y < 2.0:
                self.max_y = 2
    

        


    def x_widget(self, x, widget_width):
        return int((x - self.min_x) / (self.max_x - self.min_x) * widget_width)

    def y_widget(self, y, widget_height):
        return int(widget_height - (y - self.min_y) / (self.max_y - self.min_y) * widget_height)

    def draw_grid(self, painter, widget_width, widget_height, style):
        self.widget_width = widget_width
        self.widget_height = widget_height

        num_functions = len(self.y_values)
        total_bar_width = widget_width // (len(self.x_values) * num_functions)

        pen = QPen(style.grid_color)
        pen.setWidth(style.grid_width)
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)

        # Рисуем вертикальные линии сетки
        zero_x_mapped = self.x_widget(0, widget_width)
        for j in range(len(self.x_values)):
            x_mapped = self.x_widget(self.x_values[j], widget_width)
            if num_functions > 1:
                adjusted_x = x_mapped + (total_bar_width * num_functions) - 5
            else:
                adjusted_x = x_mapped + total_bar_width - 25
            painter.drawLine(adjusted_x, 0, adjusted_x, widget_height)

            label = f"{self.x_values[j]:.1f}"  # Format the label as needed
            painter.drawText(x_mapped + 5, widget_height - 5, label)

        # Рисуем горизонтальные линии сетки
        y_zero_mapped = self.y_widget(0, widget_height)
        max_value = int(np.ceil(np.max([abs(self.min_y), self.max_y])))
        
        
        step = int(np.ceil(max_value / 6))
        for y in range(1,max_value + 1, step):
            
            y_mapped = int(y_zero_mapped - y / self.max_y * y_zero_mapped)
            if y_mapped > 0 :
                painter.drawLine(0, y_mapped, widget_width, y_mapped)

                label = f"{y:.1f}"  # Format the label as needed
                painter.drawText(5, y_mapped, label)
            if y_mapped < widget_height:
                painter.drawLine(0, y_zero_mapped + (y_zero_mapped - y_mapped), widget_width, y_zero_mapped + (y_zero_mapped - y_mapped))

                label = f"-{y:.1f}"  # Format the label as needed
                painter.drawText(5, y_zero_mapped + (y_zero_mapped - y_mapped), label)

        # Рисуем ось X
        pen.setStyle(Qt.SolidLine)
        pen.setColor(style.grid_color)
        painter.setPen(pen)
        painter.drawLine(0, y_zero_mapped, widget_width, y_zero_mapped)


    def calculate_adjusted_x(self, x, i, j, total_bar_width):
        return x + i * total_bar_width + j + 2

    def draw_pyramid(self, painter, adjusted_x, y_zero_mapped, y_data_value, total_bar_width):
        y = self.y_widget(y_data_value, self.widget_height)
        if y_data_value > 0:
            polygon = QPolygon([
                QPoint(adjusted_x - total_bar_width // 2, y_zero_mapped),
                QPoint(adjusted_x + total_bar_width // 2, y_zero_mapped),
                QPoint(adjusted_x + total_bar_width // 2 + total_bar_width // 4, y_zero_mapped - 5),
                QPoint(adjusted_x, y)
            ])
        elif y_data_value == 0:
            polygon = QPolygon([
                QPoint(adjusted_x - total_bar_width // 2, y_zero_mapped),
            ])
        else:
            polygon = QPolygon([
                QPoint(adjusted_x + total_bar_width // 2 + total_bar_width // 4, y_zero_mapped - 5),
                QPoint(adjusted_x - total_bar_width // 2 + total_bar_width // 4, y_zero_mapped - 5),
                QPoint(adjusted_x - total_bar_width // 2, y_zero_mapped),
                QPoint(adjusted_x + total_bar_width // 2, y_zero_mapped),
                QPoint(adjusted_x, y),
                QPoint(adjusted_x - total_bar_width // 2, y_zero_mapped),
                QPoint(adjusted_x + total_bar_width // 2, y_zero_mapped),
                QPoint(adjusted_x, y)
            ])
        painter.drawPolygon(polygon)
        painter.drawLine(adjusted_x + total_bar_width // 2, y_zero_mapped, adjusted_x, y)

    def draw_plot(self, painter, widget_width, widget_height):
        bar_styles = [
            QColor(255, 0, 0),  # Красные пирамиды
            QColor(0, 255, 0),  # Зелёные пирамиды
            QColor(0, 0, 255),   # Синие пирамиды
            QColor(100,100,100)
        ]

        num_functions = len(self.y_values)
        
        total_bar_width = widget_width // (len(self.x_values) * num_functions)

        y_zero_mapped = self.y_widget(0, widget_height)

        for j in range(len(self.x_values)):
            for i, y_data in enumerate(self.y_values):
                bar_color = bar_styles[i % len(bar_styles)]
                painter.setBrush(bar_color)

                pen = QPen(Qt.black)
                pen.setWidth(1)
                painter.setPen(pen)

                x = self.x_widget(self.x_values[j], widget_width)
               
                
                adjusted_x = self.calculate_adjusted_x(x, i, j, total_bar_width)

                self.draw_pyramid(painter, adjusted_x, y_zero_mapped, y_data[j], total_bar_width)
