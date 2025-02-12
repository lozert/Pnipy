from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter
from plots import PlotStyle, PlotLine, PlotDiagram, PlotTriangle


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.plot_base = None
        self.x_values = None
        self.y_values = None

        self.setMinimumSize(600, 600)
        self.style = PlotStyle()

    def set_data(self, plot_base, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values
        self.plot_base = plot_base
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Устанавливаем фон
        painter.setBrush(self.style.background_color)
        painter.drawRect(self.rect())

        if self.plot_base == "Line Plot":
            self.plot_base = PlotLine(self.x_values, self.y_values)
        elif self.plot_base == "Diagram Plot":
            self.plot_base = PlotDiagram(self.x_values, self.y_values)
        elif self.plot_base == "Gistogram triangle":
            self.plot_base = PlotTriangle(self.x_values, self.y_values)

        if self.plot_base:
            # Рисуем сетку
            self.plot_base.draw_grid(painter, self.width(), self.height(), self.style)

            # Рисуем график
            self.plot_base.draw_plot(painter, self.width(), self.height())

        painter.end()
