from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.edit_user_window import edit_user_window

class EditUserWindow(QWidget, edit_user_window):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

    def populate_inputs(self):
        pass

    def edit_user(self):
        pass

    def check_inputs(self):
        pass