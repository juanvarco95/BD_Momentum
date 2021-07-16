from PySide2.QtWidgets import QApplication
from controllers.main_window import ListClienteWindow


if __name__ == "__main__":
    app = QApplication()
    window = ListClienteWindow()
    window.show()
    

    app.exec_()