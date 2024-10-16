import sys
import docs_maker_messages as dm
from docs_maker_gui.classes.PageSwitcher import PageSwitcher
from PySide6.QtWidgets import QApplication, QMainWindow
from docs_maker_gui.ui.docs_maker_main_window import Ui_MainWindow
from docs_maker_gui.classes.LangSwitcher import LangSwitcher
from docs_maker_gui.classes.SetUpWidgets import SetUpWidgets
from docs_maker_gui.classes.CRUD import Crud
from docs_maker_gui.classes.Configuration import Config
from docs_maker_gui.classes.DbIndicator import DbIndicator


class DocsMakerMainWindow(QMainWindow):
    def __init__(self):
        super(DocsMakerMainWindow, self).__init__()

        self.dbSession = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pageSwitcher = PageSwitcher(self.ui)
        self.crud = Crud(self.ui)
        self.config = Config(self.ui)
        self.configurations = self.config.load_config()
        self.setUpWidgets = SetUpWidgets(self.ui, self)
        self.dbIndicator = DbIndicator()
        self.setLanguage('ru')
        self.initializeUi()
        self.initializeWidgets()

    def initializeUi(self):
        self.ui.mainStacked_sw.setCurrentWidget(self.ui.mainPage_stPage)
        self.ui.main_btn.clicked.connect(self.pageSwitcher.setMainPage)
        self.ui.menu_btn.clicked.connect(self.pageSwitcher.setMenuPage)
        self.ui.menuDb_cbx.currentIndexChanged.connect(self.setUpWidgets.onMenuDbOnChange)
        self.ui.menuApply_btn.clicked.connect(self.setDbSessionManual)
        self.ui.menuDb_cbx.setCurrentText(self.configurations['database'].get('db_type'))
        self.setUpWidgets.onMenuDbOnChange()
        self.setUpWidgets.checkDatabase()
        self.setDbSessionRuntime()

    def initializeWidgets(self):
        self.ui.dbIndicator_layout.addWidget(self.dbIndicator)

    def setDbSessionManual(self):
        self.dbSession = self.setUpWidgets.applyBtn()
        self.setUpWidgets.checkDatabase()
        self.setUpWidgets.setInformation()

    def setDbSessionRuntime(self):
        if self.configurations['database'].get('db_type'):
            self.dbSession = self.setUpWidgets.runDbConnection()
        self.setUpWidgets.checkDatabase()
        self.setUpWidgets.setInformation()

    def setLanguage(self, lang_code):
        self.tr = dm.set_language(lang_code)
        self.setUpWidgets.tr = self.tr
        self.setWindowTitle(self.tr.gettext('App Title'))
        LangSwitcher(self.ui, self).translateSetter(self.tr)


def docsMakerRun():
    app = QApplication(sys.argv)
    window = DocsMakerMainWindow()
    window.show()
    sys.exit(app.exec())
