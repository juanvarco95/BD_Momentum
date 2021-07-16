from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.pdf_window import pdf_create

class PDFWindow(QWidget, pdf_create):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

    def check_inputs(self):
        pass

    def createPDF(self):
        pass