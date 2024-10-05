import sys
import docs_maker_messages as dm

from docs_maker_gui.classes.PageSwitcher import PageSwitcher

from PySide6.QtWidgets import QApplication, QMainWindow
from docs_maker_gui.ui.docs_maker_main_window import Ui_MainWindow 

class DocsMakerMainWindow(QMainWindow):
    def __init__(self):
        super(DocsMakerMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pageSwitcher = PageSwitcher(self.ui)
        self.initializeUi()

    def initializeUi(self):
        self.ui.mainStacked_sw.setCurrentWidget(self.ui.mainPage_stPage)
        self.ui.main_btn.clicked.connect(self.pageSwitcher.setMainPage)
        self.ui.menu_btn.clicked.connect(self.pageSwitcher.setMenuPage)

    def setLanguage(self, lang_code):
        l = dm.set_language(lang_code)

        self.setWindowTitle(l.gettext('App Title'))
        self.ui.mainWindow_lbl.setText((l.gettext('MainPage')))
        self.ui.menu_lbl.setText(l.gettext('MenuPage'))

def docsMakerRun():
    app = QApplication(sys.argv)
    window = DocsMakerMainWindow()
    window.setLanguage('ru')
    window.show()
    sys.exit(app.exec())
