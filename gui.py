import PyQt6.QtWidgets


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        label = PyQt6.QtWidgets.QLabel("Hello World!")
        label.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


app = PyQt6.QtWidgets.QApplication([])
window = MainWindow()
window.show()

app.exec()
