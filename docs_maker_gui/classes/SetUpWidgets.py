from gettext import GNUTranslations
from typing import Optional
import sqlalchemy.exc
from PySide6.QtGui import QColor, QPainter, QPixmap
from sqlalchemy.orm import Session
from docs_maker.database.init_db_postgres import InitDbPostgres
from docs_maker_gui.ui.docs_maker_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMessageBox
from docs_maker.database.init_db_sqlite3 import InitDbSqlite3
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt, QSize


class SetUpWidgets:
    def __init__(self, ui: Ui_MainWindow, parent, translate: Optional[GNUTranslations] = None):
        self.__ui = ui
        self.__parent = parent
        self.__tr = translate

    @property
    def ui(self):
        return self.__ui

    @property
    def parent(self):
        return self.__parent

    @property
    def tr(self):
        return self.__tr

    @tr.setter
    def tr(self, data):
        self.__tr = data

    def onMenuDbOnChange(self):
        self.loadConfiguration(self.parent.configurations)
        if self.ui.menuDb_cbx.currentText() == 'SQLite3':
            self.ui.menuDbHost_le.setText('')
            self.ui.menuDbPort_le.setText('')
            self.ui.menuDbUsername_le.setText('')
            self.ui.menuDbPassword_le.setText('')
            self.ui.menuDbHost_le.setEnabled(False)
            self.ui.menuDbPort_le.setEnabled(False)
            self.ui.menuDbUsername_le.setEnabled(False)
            self.ui.menuDbPassword_le.setEnabled(False)
        elif self.ui.menuDb_cbx.currentText() == 'PostgreSQL':
            self.ui.menuDbHost_le.setEnabled(True)
            self.ui.menuDbPort_le.setEnabled(True)
            self.ui.menuDbUsername_le.setEnabled(True)
            self.ui.menuDbPassword_le.setEnabled(True)

    def loadConfiguration(self, config):
        if self.ui.menuDb_cbx.currentText() == 'SQLite3':
            self.ui.menuDbName_le.setText(config['database'].get('db_name'))
        elif self.ui.menuDb_cbx.currentText() == 'PostgreSQL':
            self.ui.menuDbName_le.setText(config['database'].get('db_name'))
            self.ui.menuDbHost_le.setText(config['database'].get('db_host'))
            self.ui.menuDbPort_le.setText(config['database'].get('db_port'))
            self.ui.menuDbUsername_le.setText(config['database'].get('db_username'))
            self.ui.menuDbPassword_le.setText(config['database'].get('db_password'))
        else:
            self.ui.menuDb_cbx.setCurrentText('SQLite3')

    def applyBtn(self) -> Session:
        db_session, result = self.initDb()
        if result:
            self.parent.config.save_config()
            QMessageBox.information(self.parent, self.tr.gettext('Information'), self.tr.gettext('Apply config'),
                                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            self.parent.configurations = self.parent.config.load_config()

        return db_session

    def runDbConnection(self) -> Session:
        db_session, result = self.initDb()

        return db_session

    def initDb(self):
        if self.ui.menuDb_cbx.currentText() == 'SQLite3':
            sqlite_session = InitDbSqlite3(self.ui.menuDbName_le.text())
            db_session = sqlite_session.init()

            return db_session, True

        elif self.ui.menuDb_cbx.currentText() == 'PostgreSQL':
            postgresql_session = InitDbPostgres(self.ui.menuDbUsername_le.text(), self.ui.menuDbPassword_le.text(),
                                                self.ui.menuDbHost_le.text(), self.ui.menuDbPort_le.text(),
                                                self.ui.menuDbName_le.text())
            try:
                db_session = postgresql_session.init()

                return db_session, True

            except sqlalchemy.exc.OperationalError as e:
                QMessageBox.critical(self.parent, self.tr.gettext('Error'), str(e),
                                     QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

        return None, False

    def checkDatabase(self):
        db_type = self.parent.configurations['database'].get('db_type')
        if db_type:
            self.parent.dbIndicator.ui.db_type.setText(db_type)
        else:
            self.parent.dbIndicator.ui.db_type.setText(self.tr.gettext('No db type'))

    def setInformation(self):
        if not self.parent.dbSession:
            self.parent.dbIndicator.ui.information.setText(self.tr.gettext('Db is not connected'))
            self.parent.dbIndicator.ui.information.setStyleSheet("color: red;")
            color = QColor("red")
            self.updateLightColor(color)

            return False

        if self.parent.dbSession.is_active:
            self.parent.dbIndicator.ui.information.setText(self.tr.gettext('Db is Connected'))
            self.parent.dbIndicator.ui.information.setStyleSheet("color: green;")
            color = QColor("green")
            self.updateLightColor(color)

            return True

    def updateLightColor(self, color):
        pixmap = QPixmap(QSize(24, 24))
        pixmap.fill(QColor(Qt.transparent))

        painter = QPainter(pixmap)

        svg_render = QSvgRenderer(":icons/icons/light-64-gray.svg")
        svg_render.render(painter)

        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)

        painter.end()

        self.parent.dbIndicator.ui.db_status.setPixmap(pixmap)
