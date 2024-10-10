from PySide6.QtWidgets import QWidget
from docs_maker_gui.ui.db_indicator import Ui_Form


class DbIndicator(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()

        self.ui.setupUi(self)
