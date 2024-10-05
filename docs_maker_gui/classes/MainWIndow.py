import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from docs_maker_gui.ui.docs_maker_main_window import Ui_MainWindow 

class DocsMakerMainWindow(QMainWindow):
    def __init__(self):
        super(DocsMakerMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def docsMakerRun():
    app = QApplication(sys.argv)
    window = DocsMakerMainWindow()
    window.show()
    sys.exit(app.exec())
