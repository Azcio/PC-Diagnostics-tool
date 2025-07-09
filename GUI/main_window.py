from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget,
    QTabWidget, QHBoxLayout
)
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import psutil

from diagnostics.system_info import get_system_info
from diagnostics.performance import get_performance
from diagnostics.hardware_check import check_disk_health, check_memory
from reports.report_generator import generate_report


class LiveChart(QWidget):
    def __init__(self):
        super().__init__()
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.ax = self.figure.add_subplot(111)
        self.cpu_data = []
        self.ram_data = []
        self.time_data = []
        self.counter = 0

        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 second
        self.timer.timeout.connect(self.update_chart)
        self.timer.start()

    def update_chart(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        self.cpu_data.append(cpu)
        self.ram_data.append(ram)
        self.time_data.append(self.counter)
        self.counter += 1

        # Keep only the last 60 points
        if len(self.cpu_data) > 60:
            self.cpu_data.pop(0)
            self.ram_data.pop(0)
            self.time_data.pop(0)

        self.ax.clear()
        self.ax.plot(self.time_data, self.cpu_data, label="CPU (%)", color="blue")
        self.ax.plot(self.time_data, self.ram_data, label="RAM (%)", color="green")
        self.ax.set_ylim(0, 100)
        self.ax.set_title("Live CPU & RAM Usage")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Usage (%)")
        self.ax.legend(loc="upper right")
        self.canvas.draw()


class ReportTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button = QPushButton("Run Diagnostics")
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.button.clicked.connect(self.run_diagnostics)
        layout.addWidget(self.button)
        layout.addWidget(self.text_area)
        self.setLayout(layout)

    def run_diagnostics(self):
        sys_info = get_system_info()
        perf = get_performance()
        disk_health = check_disk_health()
        memory_health = check_memory()
        diagnostics = [disk_health, memory_health]
        report = generate_report(sys_info, perf, diagnostics)
        self.text_area.setPlainText(report)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Diagnostic Tool")
        self.resize(900, 600)

        tabs = QTabWidget()
        tabs.addTab(LiveChart(), "📊 Live Stats")
        tabs.addTab(ReportTab(), "📋 System Report")

        container = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(tabs)
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
